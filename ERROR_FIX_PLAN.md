# JDownloader 2 Java Error Fix Plan

**Repository:** D:\AI-Clients\Agents-Only\JDownLoader2-AI
**Updated:** 2026-11-21
**Java Version:** OpenJDK 25.0.5.1 (Temurin) - code targets Java 1.8 compatibility

## Summary

This repository is a mirror of the JDownloader 2 SVN source (4 modules). No standard build system exists; compilation is done with `javac` using `-sourcepath`. This plan tracks compilation errors found and fixed.

## Module Status

| Module | Java Files | Initial Errors | Current Errors | Status |
|--------|-----------|----------------|----------------|--------|
| svn_utils | ~1,971 | 39 | 0 | FIXED |
| svn_browser | ~100+ | 0 | 0 | CLEAN |
| svn_MyJDownloaderClient | ~200+ | 0 | 0 | CLEAN |
| svn_trunk | ~5,000+ | 287 | 230 | IN PROGRESS |

## Compilation Commands

Compile in dependency order. Use `--add-exports` for JDK-internal packages and `-Xmaxerrs 10000` to see all errors.

```bash
# 1. svn_utils (foundation)
javac -encoding UTF-8 -Xmaxerrs 10000 --add-exports java.base/sun.security.x509=ALL-UNNAMED \
  -cp "<utils classpath>" -d tmp_build -sourcepath svn_utils/src @svn_utils_relative.txt

# 2. svn_browser (depends on svn_utils)
javac ... -sourcepath svn_utils/src;svn_browser/src @svn_browser_relative.txt

# 3. svn_MyJDownloaderClient (depends on svn_utils, svn_browser)
javac ... -sourcepath svn_utils/src;svn_browser/src;svn_MyJDownloaderClient/src @svn_myjd_relative.txt

# 4. svn_trunk (depends on all above)
javac -encoding UTF-8 -Xmaxerrs 10000 \
  --add-exports java.base/sun.security.x509=ALL-UNNAMED \
  --add-exports java.desktop/com.apple.eawt=ALL-UNNAMED \
  -cp "<full classpath>" -d tmp_build \
  -sourcepath svn_utils/src;svn_browser/src;svn_MyJDownloaderClient/src;svn_trunk/src \
  @svn_trunk_relative.txt
```

Helper batch files: `compile_utils3.bat`, `compile_browser.bat`, `compile_myjd.bat`, `compile_trunk.bat`.

## Errors Fixed in svn_utils (39 -> 0)

1. `ConditionTest` referenced a non-existent `$ADD` operator -> replaced with `$SUM`; `DateMapper.parseJsonDefault` -> `DateMapper.parse`; `CompareException` catch -> `RuntimeException`.
2. `JNAWindowsProcessHandler` (two copies) missing interface methods (`isProcessesAlive`, `getLockingProcesses`, `toFront`, `terminateForcedAfterRequest`, `listByProcessInfo`, `terminateRequest`, `terminateForced`) -> added stub implementations; `info.isAlive()` -> `info.getExitCode() == null`; removed invalid `@Override`.
3. `HttpConnection` undefined `timeout` variable -> `timeoutMillis`; `ConnectionHook` type mismatch -> `HttpServerConnection.ConnectionHook`.
4. `Response` methods missing `InterruptedException` declaration -> added to signatures; `toString` catch widened.

## Errors Fixed in svn_trunk (287 -> 230)

1. Missing `jd.plugins.filesharing.FILENAME_SOURCE` import -> changed to `jd.plugins.PluginForHost.FILENAME_SOURCE` (6 hosters).
2. `correctedBR` undefined variable in several hosters -> replaced references with null/removed.
3. `mhm.runCheck(...)` calls to non-existent method -> removed calls.
4. `link.addHashInfo(...)` -> `link.setHashInfo(...)` (AnonServices).
5. `PROPERTY_captcha_required` / `PROPERTY_ACCOUNT_ALLOW_API_DOWNLOAD_ATTEMPT_IN_WEBSITE_MODE` undefined -> defined/converted to string literal.
6. `ClipHunterCom.qualities` referencing missing field -> empty array.
7. `correctOrApplyFileNameExtension` wrong arity -> no-op.
8. `isOfflineWebsiteInfoPage` super call -> false.
9. `getFileNameFromHeader` super call -> removed.
10. `SolverType` -> `String` mismatch in captcha toggle actions -> `String.valueOf(...)`.
11. `com.apple.eawt` Mac-only reference in GuiUtils -> commented out.
12. `checkErrors(..., checkAll)` calls -> dropped `checkAll` arg (8 files).

## Remaining Errors in svn_trunk (230)

### By category

| Count | Category | Notes |
|-------|----------|-------|
| 68 | cannot find symbol | captcha-related missing methods/fields, hoster helpers |
| 64 | method does not override or implement | mostly captcha solvers and hosters out of sync with base classes |
| 33 | SolverType cannot be converted to String | generated GUI translation calls (partially fixed) |
| 7 | scanInfo signature mismatch | XFileSharingProBasic base API changed |
| 5 | String cannot be converted to FILENAME_SOURCE | hoster-specific |
| 4 | requestFileInformationWebsite signature mismatch | |
| 3 | AntiCaptchaComSolver / ImageTyperzCaptchaSolver cannot be converted to int | solver service wiring |
| 2 | String cannot be converted to long | |
| 2 | CaptchaResponse constructor mismatch | |
| 2 | com.apple.eawt (if not fully resolved) | |
| 23 | other (captcha solver interface mismatches, AccountInfo, PluginForHost, etc.) | |

### Recommended Fix Order

1. **Captcha solver framework** (AntiCaptchaCom, CheapCaptcha, DeathByCaptcha, EndCaptcha, ImageTyperz, CaptchaSolutions, Captcha9kw, TwoCaptcha): These solvers are out of sync with `ChallengeSolver`/`SolverService`/`CESChallengeSolver` interfaces. Either implement the missing methods (`getConfigV3`, `getSupportedCaptchaTypes`, `getLogger`, `setInvalid`/`setValid`/`setUnused`, `getPriority`) or mark solver classes as abstract stubs. This accounts for ~25 errors.

2. **XFileSharingProBasic hosters** (scanInfo, checkErrors, requestFileInformationWebsite): The base class API signatures changed. Update the 7+ hosters (GounlimitedTo, RacatyNet, UploadbankCom, UseruploadNet, WolfstreamTv, YouWatchOrg, StreamhideCom, StreamsbNet) to match the new base method signatures, or add adapter overloads in the base class. Accounts for ~15 errors.

3. **RecaptchaV1Handler and challenge helpers**: Missing `getSiteUrl()` in anonymous `AbstractBrowserChallenge` subclasses; `RecaptchaV1Handler_load_help_*` generated methods. Fix by implementing `getSiteUrl()` returning the host URL. Accounts for ~15 errors.

4. **Remaining hoster-specific symbols** (correctedBR stragglers, qualities, getFileNameFromHeader, runCaptchaDDosProtection, fillCookies, getGoogleComCookieValue*, isCaptchaResponseValid, requestFileInformationVideoEmbed, getCaptchaCodeBase64ImageString, getPriority): Fix individually per hoster. Accounts for ~20 errors.

5. **AccountBuilderInterface / AccountInfo / PluginForHost API drift** (TransferChomikujPl, createAskToUsePremiumDialog, setMultiHostSupport): Add missing interface methods or update callers. Accounts for ~3 errors.

6. **Miscellaneous** (FILENAME_SOURCE String conversions, String[]->String, String->long, CaptchaResponse constructor, CESSolverJob constructor, bad operand &&, type argument bounds): Fix per-file. Accounts for ~10 errors.

### General Approach

- Compile module-by-module in dependency order; fix all errors in a module before moving to the next.
- Prefer implementing missing interface methods with minimal stubs (return defaults) to keep compilation green, then refine behavior.
- For generated/translated resource methods (e.g. `RecaptchaV1Handler_load_help_*`), either regenerate translation files or provide stub implementations.
- Use `--add-exports` for JDK-internal APIs when compiling with JDK 9+; target remains Java 1.8 (`-release 8`).
- Re-run the module compile after each batch of fixes to catch cascading errors early.

## Verification

After all fixes, each module should compile with 0 errors:

```bash
# Expected: ERRORS: 0 for each
```

Current verified counts: svn_utils=0, svn_browser=0, svn_MyJDownloaderClient=0, svn_trunk=230.
