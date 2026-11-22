"""Build a standalone Windows 11 JDownloader 2 distribution into ./dist/."""

import json
import os
import shutil
import subprocess
import sys
import time
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CLS = ROOT / "tmp_build"
DIST = ROOT / "dist"


def find_rc_exe() -> Path | None:
    kits = Path(r"C:\Program Files (x86)\Windows Kits\10\bin")
    if kits.exists():
        matches = sorted(kits.glob("*/x64/rc.exe"), reverse=True)
        if matches:
            return matches[0]
    found = shutil.which("rc.exe")
    return Path(found) if found else None


def compile_java_if_needed() -> None:
    if CLS.exists() and any(CLS.rglob("*.class")):
        return
    for bat in ["compile_utils3.bat", "compile_browser.bat", "compile_myjd.bat", "compile_trunk.bat"]:
        print(f"Running {bat}...")
        subprocess.run(["cmd.exe", "/c", str(ROOT / bat)], cwd=str(ROOT), check=True)


def copy_tree(src: Path, dst: Path, exclude_exts=(".psd", ".pnd")) -> None:
    if not src.exists():
        return
    for root, _, files in os.walk(src):
        rel = Path(root).relative_to(src)
        out_dir = dst / rel
        out_dir.mkdir(parents=True, exist_ok=True)
        for fn in files:
            if any(fn.endswith(e) for e in exclude_exts):
                continue
            shutil.copy2(Path(root) / fn, out_dir / fn)


def collect_files(base: Path, include_fn):
    out = []
    if not base.exists():
        return out
    for root, _, files in os.walk(base):
        for fn in files:
            p = Path(root) / fn
            rel = p.relative_to(base).as_posix()
            if include_fn(rel):
                out.append((p, rel))
    return out


def make_jar(jar_path: Path, entries: list[tuple[Path, str]], manifest_lines: list[str] | None = None) -> None:
    jar_path.parent.mkdir(parents=True, exist_ok=True)
    seen = set()
    with zipfile.ZipFile(jar_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        if manifest_lines:
            mf = "\r\n".join(manifest_lines) + "\r\n"
            zf.writestr("META-INF/MANIFEST.MF", mf.encode("utf-8"))
            seen.add("META-INF/MANIFEST.MF")
        for base, arcname in entries:
            arcname = arcname.replace("\\", "/")
            if arcname in seen:
                continue
            seen.add(arcname)
            zf.write(base, arcname)


def build_dist() -> None:
    compile_java_if_needed()

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)

    print("1. Copying resources, libs, themes, translations, and compiled plugins...")
    copy_tree(ROOT / "svn_trunk/ressourcen/jd", DIST / "jd")
    copy_tree(ROOT / "svn_trunk/ressourcen/tools", DIST / "tools")
    copy_tree(ROOT / "svn_utils/themes/themes/standard/org/appwork", DIST / "themes/standard/org/jdownloader")
    copy_tree(ROOT / "svn_trunk/themes", DIST)

    libs_dir = DIST / "libs"
    libs_dir.mkdir(parents=True, exist_ok=True)
    for src_dir, skip in [
        (ROOT / "svn_trunk/ressourcen/libs", {"proxyVole.jar", "jna.jar", "jna_platform.jar"}),
        (ROOT / "svn_utils/libs", {"miglayout.jar", "miglayout-core.jar"}),
        (ROOT / "svn_browser/libs", set()),
    ]:
        for p, rel in collect_files(src_dir, lambda r: not r.endswith(".info") and not r.endswith("-sources.jar") and Path(r).name not in skip):
            dst = libs_dir / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, dst)

    trans_dir = DIST / "translations"
    trans_dir.mkdir(parents=True, exist_ok=True)
    for src in [ROOT / "svn_utils/src", ROOT / "svn_browser/src", ROOT / "svn_trunk/src"]:
        for p, rel in collect_files(src, lambda r: r.endswith(".lng")):
            dst = trans_dir / rel
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(p, dst)
    for p, rel in collect_files(ROOT / "svn_trunk/translations", lambda r: r.endswith(".lng")):
        dst = DIST / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dst)

    copy_tree(CLS / "jd/plugins/hoster", DIST / "jd/plugins/hoster")
    copy_tree(CLS / "jd/plugins/decrypter", DIST / "jd/plugins/decrypter")
    (DIST / "build.json").write_text(
        json.dumps({"buildDate": time.strftime("%a %b %d %H:%M:%S UTC %Y", time.gmtime())}, indent=2),
        encoding="utf-8",
    )

    print("2. Building component and extension JARs...")
    make_jar(DIST / "libs/JDGUI.jar", collect_files(CLS, lambda r: r.startswith("jd/gui/")))
    make_jar(DIST / "libs/JAntiCaptcha.jar", collect_files(CLS, lambda r: r.startswith("jd/captcha/") and not r.startswith("jd/captcha/methods/")))
    make_jar(DIST / "libs/cons.jar", collect_files(CLS, lambda r: r.startswith("org/jdownloader/container/")))
    make_jar(
        DIST / "libs/laf/syntheticaJDCustom.jar",
        collect_files(CLS, lambda r: r.startswith("org/jdownloader/gui/laf/") and not r.startswith("org/jdownloader/gui/laf/plain/"))
        + collect_files(ROOT / "svn_trunk/src", lambda r: r.startswith("org/jdownloader/gui/laf/") and not r.startswith("org/jdownloader/gui/laf/plain/") and not r.endswith(".java")),
    )
    make_jar(
        DIST / "libs/laf/syntheticaJDPlain.jar",
        collect_files(CLS, lambda r: r.startswith("org/jdownloader/gui/laf/plain/"))
        + collect_files(ROOT / "svn_trunk/src", lambda r: r.startswith("org/jdownloader/gui/laf/plain/") and not r.endswith(".java")),
    )

    addons = [
        ("EventScripter", "eventscripter"),
        ("JDChat", "chat"),
        ("infobar", "infobar"),
        ("FolderWatch", "folderwatchV2"),
        ("JDShutdown", "shutdown"),
        ("JDGrowl", "growl"),
        ("AntiShutdown", "antistandby"),
        ("Extraction", "extraction"),
        ("Scheduler", "schedulerV2"),
        ("translator", "translator"),
    ]
    for pkg, inc in addons:
        make_jar(
            DIST / f"extensions/{pkg}.jar",
            collect_files(CLS, lambda r, inc=inc: r.startswith(f"org/jdownloader/extensions/{inc}/"))
            + collect_files(ROOT / "svn_trunk/src", lambda r, inc=inc: r.startswith(f"org/jdownloader/extensions/{inc}/") and not r.endswith(".java")),
        )

    print("3. Building Core.jar...")
    core_excludes = (
        "jd/captcha/",
        "org/appwork/",
        "org/jdownloader/gui/laf/",
        "org/jdownloader/update/",
        "org/jdownloader/launcher/",
        "org/jdownloader/uninstaller/",
        "org/jdownloader/installer/",
        "jd/gui/",
        "com/fastcgi/",
        "org/jdownloader/updatev2/",
        "jd/http/",
        "jd/plugins/hoster/",
        "jd/plugins/decrypter/",
        "jd/utils/dev/",
        "tests/",
    )

    def core_cls_filter(r: str) -> bool:
        if not (r.endswith(".class") or r.endswith(".txt") or r.endswith(".dat")):
            return False
        if r.startswith("org/jdownloader/container/") or r.startswith("jd/nutils/"):
            return True
        if "/test/" in r:
            return False
        if r.startswith("org/jdownloader/extensions/") and r.count("/") >= 4:
            return False
        if r.startswith("jd/controlling/reconnect/plugins/") and r.count("/") >= 5:
            return False
        return not any(r.startswith(ex) for ex in core_excludes)

    core_entries = (
        collect_files(CLS, core_cls_filter)
        + collect_files(
            ROOT / "svn_trunk/src",
            lambda r: r.endswith((".js", ".html", ".css"))
            or r.startswith("org/jdownloader/captcha/v2/solver/browser/html/")
            or (r.startswith("org/jdownloader/captcha/v2/challenge/recaptcha/v2/example/") and r.endswith(".jpg")),
        )
        + collect_files(ROOT / "svn_trunk/ressourcen", lambda r: r.endswith(".properties") and "/" not in r)
    )
    make_jar(DIST / "Core.jar", core_entries, ["Manifest-Version: 1.0", "Created-By: AppWork GmbH and JDownloader Community"])

    print("4. Building JDownloader.jar...")
    cp_list = ["Core.jar"]
    cp_list += sorted(p.relative_to(DIST).as_posix() for p in (DIST / "libs").rglob("*.jar"))
    cp_list += sorted(p.relative_to(DIST).as_posix() for p in (DIST / "extensions").rglob("*.jar"))

    launcher_entries = []
    seen_arc = {"META-INF/MANIFEST.MF"}

    def add_entry(arc: str, data: bytes) -> None:
        if arc in seen_arc:
            return
        seen_arc.add(arc)
        launcher_entries.append((arc, data))

    for embed_jar in [
        ROOT / "svn_utils/libs/miglayout.jar",
        ROOT / "svn_utils/libs/miglayout-core.jar",
        ROOT / "svn_trunk/ressourcen/libs/proxyVole.jar",
        ROOT / "svn_trunk/ressourcen/libs/jna.jar",
        ROOT / "svn_trunk/ressourcen/libs/jna_platform.jar",
    ]:
        with zipfile.ZipFile(embed_jar, "r") as ez:
            for info in ez.infolist():
                if info.is_dir():
                    continue
                n = info.filename
                if n.endswith("MANIFEST.MF") or n.startswith("META-INF/") or n == "module-info.class":
                    continue
                add_entry(n, ez.read(n))

    add_entry("classpath", ("\n".join(cp_list) + "\n").encode("utf-8"))

    launcher_includes = (
        "jd/Main.class",
        "org/jdownloader/launcher/",
        "org/jdownloader/logging/",
        "org/jdownloader/updatev2/",
        "org/jdownloader/update/",
        "org/jdownloader/uninstaller/",
        "org/jdownloader/installer/",
        "jd/http/",
        "org/appwork/",
    )
    launcher_excludes = ("org/appwork/update/server/", "org/appwork/utils/sms/", "org/appwork/utils/ide/")

    for p, rel in collect_files(CLS, lambda r: r.startswith(launcher_includes) and not r.startswith(launcher_excludes)):
        add_entry(rel, p.read_bytes())

    for p, rel in collect_files(
        ROOT / "svn_utils/src",
        lambda r: r == "org/appwork/utils/net/effective_tld_names.dat"
        or (r.startswith("org/appwork/remoteapi/html/") and r.endswith((".css", ".js", ".html"))),
    ):
        add_entry(rel, p.read_bytes())

    for p, rel in collect_files(
        ROOT / "svn_trunk/themes",
        lambda r: r.startswith("themes/standard/") and ("/images/dialog/" in r or "/images/update" in r) and not r.endswith((".psd", ".pnd")),
    ):
        add_entry(rel, p.read_bytes())

    manifest = "\r\n".join([
        "Manifest-Version: 1.0",
        "Created-By: AppWork GmbH and JDownloader Community",
        "Main-Class: org.jdownloader.launcher.JDLauncher",
        "Add-Exports: java.desktop/sun.swing java.desktop/sun.swing.table java.desktop/sun.swing.plaf.synth java.desktop/com.sun.java.swing.plaf.windows java.desktop/sun.awt.shell java.desktop/com.sun.awt java.base/sun.security.action",
        "Add-Opens: java.desktop/javax.swing.plaf.synth java.desktop/javax.swing.plaf.basic java.desktop/javax.swing java.desktop/javax.swing.tree java.desktop/java.awt.event",
    ]) + "\r\n"

    with zipfile.ZipFile(DIST / "JDownloader.jar", "w", compression=zipfile.ZIP_DEFLATED) as zf:
        zf.writestr("META-INF/MANIFEST.MF", manifest.encode("utf-8"))
        for arc, data in launcher_entries:
            zf.writestr(arc, data)

    print("5. Building JDownloader2.exe (Windows launcher)...")
    rustc = shutil.which("rustc")
    if not rustc:
        raise RuntimeError("rustc not found in PATH")
    rc_exe = find_rc_exe()
    res_file = ROOT / "tmp_build/jdownloader2.res"
    rustc_args = [
        rustc,
        str(ROOT / "launcher/jdownloader2.rs"),
        "--edition",
        "2024",
        "-O",
        "-C",
        "strip=symbols",
        "--crate-type",
        "bin",
        "-o",
        str(DIST / "JDownloader2.exe"),
    ]
    if rc_exe:
        subprocess.run(
            [str(rc_exe), "/nologo", "/fo", str(res_file), str(ROOT / "launcher/jdownloader2.rc")],
            cwd=str(ROOT / "launcher"),
            check=True,
        )
        rustc_args.extend(["-C", f"link-arg={res_file}"])
    subprocess.run(rustc_args, cwd=str(ROOT), check=True)
    if res_file.exists():
        res_file.unlink()
    pdb_file = DIST / "JDownloader2.pdb"
    if pdb_file.exists():
        pdb_file.unlink()

    print(f"Done! Windows build ready at: {DIST / 'JDownloader2.exe'}")


if __name__ == "__main__":
    build_dist()

