#![windows_subsystem = "windows"]

use std::env;
use std::ffi::OsStr;
use std::os::windows::ffi::OsStrExt;
use std::path::{Path, PathBuf};
use std::process::{Command, Stdio};
use std::ptr;

const MB_OK: u32 = 0x0000_0000;
const MB_ICONERROR: u32 = 0x0000_0010;
const ATTACH_PARENT_PROCESS: u32 = 0xFFFF_FFFF;

#[link(name = "user32")]
unsafe extern "system" {
    fn MessageBoxW(hwnd: *mut core::ffi::c_void, text: *const u16, caption: *const u16, utype: u32) -> i32;
}

#[link(name = "kernel32")]
unsafe extern "system" {
    fn AttachConsole(dw_process_id: u32) -> i32;
}

fn to_wide(s: &str) -> Vec<u16> {
    OsStr::new(s).encode_wide().chain(std::iter::once(0)).collect()
}

fn show_error(msg: &str) {
    let text = to_wide(msg);
    let title = to_wide("JDownloader 2 Launcher Error");
    unsafe {
        MessageBoxW(ptr::null_mut(), text.as_ptr(), title.as_ptr(), MB_OK | MB_ICONERROR);
    }
}

fn is_console_mode(args: &[String]) -> bool {
    args.iter().any(|a| {
        matches!(
            a.to_ascii_lowercase().as_str(),
            "-h" | "--help" | "-help" | "-?" | "-console" | "-threaddump"
        )
    })
}

fn find_java(exe_dir: &Path, console: bool) -> Option<PathBuf> {
    let bin_name = if console { "java.exe" } else { "javaw.exe" };

    // 1. Bundled JRE next to JDownloader2.exe
    for sub in ["jre", "java", "runtime"] {
        let candidate = exe_dir.join(sub).join("bin").join(bin_name);
        if candidate.is_file() {
            return Some(candidate);
        }
    }

    // 2. JAVA_HOME
    if let Some(java_home) = env::var_os("JAVA_HOME") {
        let candidate = PathBuf::from(java_home).join("bin").join(bin_name);
        if candidate.is_file() {
            return Some(candidate);
        }
    }

    // 3. PATH
    if let Some(path_var) = env::var_os("PATH") {
        for dir in env::split_paths(&path_var) {
            let candidate = dir.join(bin_name);
            if candidate.is_file() {
                return Some(candidate);
            }
        }
    }

    // 4. Standard Windows JDK/JRE install locations (newest folder first)
    let vendors = [
        r"C:\Program Files\Eclipse Adoptium",
        r"C:\Program Files\Java",
        r"C:\Program Files\Microsoft",
        r"C:\Program Files\Amazon Corretto",
        r"C:\Program Files\Zulu",
        r"C:\Program Files\BellSoft",
    ];
    let mut candidates: Vec<PathBuf> = Vec::new();
    for vendor in vendors {
        if let Ok(entries) = std::fs::read_dir(vendor) {
            for entry in entries.flatten() {
                let candidate = entry.path().join("bin").join(bin_name);
                if candidate.is_file() {
                    candidates.push(candidate);
                }
            }
        }
    }
    candidates.sort();
    candidates.pop()
}

fn main() {
    let exe_path = match env::current_exe() {
        Ok(p) => p,
        Err(e) => {
            show_error(&format!("Failed to locate executable path: {e}"));
            std::process::exit(1);
        }
    };
    let exe_dir = match exe_path.parent() {
        Some(p) => p.to_path_buf(),
        None => {
            show_error("Failed to determine application directory.");
            std::process::exit(1);
        }
    };

    let jar_path = exe_dir.join("JDownloader.jar");
    if !jar_path.is_file() {
        show_error(&format!(
            "Could not find JDownloader.jar in:\n{}",
            exe_dir.display()
        ));
        std::process::exit(1);
    }

    let args: Vec<String> = env::args().skip(1).collect();
    let console = is_console_mode(&args);

    let java_exe = match find_java(&exe_dir, console) {
        Some(p) => p,
        None => {
            show_error(
                "Could not find a Java runtime (javaw.exe / java.exe).\n\
                 Please install Java (JDK/JRE) or set JAVA_HOME.",
            );
            std::process::exit(1);
        }
    };

    if console {
        unsafe {
            AttachConsole(ATTACH_PARENT_PROCESS);
        }
    }

    let mut cmd = Command::new(&java_exe);
    cmd.current_dir(&exe_dir);
    cmd.arg("-jar").arg(&jar_path).args(&args);

    if console {
        cmd.stdin(Stdio::inherit())
            .stdout(Stdio::inherit())
            .stderr(Stdio::inherit());
        match cmd.status() {
            Ok(status) => std::process::exit(status.code().unwrap_or(0)),
            Err(e) => {
                show_error(&format!("Failed to start JDownloader 2: {e}"));
                std::process::exit(1);
            }
        }
    } else {
        cmd.stdin(Stdio::null())
            .stdout(Stdio::null())
            .stderr(Stdio::null());
        if let Err(e) = cmd.spawn() {
            show_error(&format!("Failed to start JDownloader 2: {e}"));
            std::process::exit(1);
        }
    }
}
