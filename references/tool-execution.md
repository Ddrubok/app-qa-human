# Tool execution protocol

Use the available host's tools and existing project framework. Establish platform/build, chosen device or browser context, version, available input methods, capture/viewer support and test boundary before acting. Do not install a mobile stack for a small review. A tool's existence does not establish device access or safe service isolation.

For each interaction: observe state and target → act through the relevant input → wait for a meaningful condition with a bounded wait → observe outcome → record evidence and restore changed state. Use stable accessible labels/IDs before coordinates. Re-resolve targets after navigation/layout changes. Command exit 0 is not an application pass. Never retry an ambiguous irreversible action blindly.

## Existing browser tools

Prefer the host browser interface or installed Playwright/Puppeteer. In Playwright, typical operations are `page.getByRole('button', {name: 'Save'}).click()`, `page.getByLabel('Title').fill(value)`, `page.keyboard.press('Tab')`, `page.goBack()`, and `page.screenshot({path})` when capture is allowed. Wait on the expected visible state/response and verify the stored outcome. Equivalent Puppeteer locators/actions are acceptable; verify the installed API rather than assuming identical syntax. `evaluate(() => handler())` does not prove pointer reachability. Filling text does not test an actual mobile keyboard or IME.

## Android ADB fallback

Enumerate with `adb devices -l`, select the intended authorized device, and pass `-s SERIAL` on each device command. Read local `adb shell input --help`/tool help when syntax varies. Common operations: `adb -s SERIAL shell input tap X Y`, `... input text SAFE_ASCII`, `... input keyevent KEYCODE_BACK`. Coordinates need a current observation; quote/encode values safely instead of interpolating untrusted input into a shell.

For permitted capture, `adb -s SERIAL shell screencap -p /sdcard/qa-RUN-CASE.png` then `adb -s SERIAL pull /sdcard/qa-RUN-CASE.png LOCAL_PATH` avoids text-shell binary redirection. Use an app/test-owned unique temporary path, inspect the pulled file when possible, then remove only that known temporary capture. Respect privacy before creating the device file. ADB text injection cannot prove Korean IME/emoji entry works on the user's keyboard.

## Maestro, Appium and iOS

If Maestro is already configured, map intents to its installed `tapOn`, `inputText`, `back`, `takeScreenshot`, `assertVisible` and wait commands; validate version and platform support before generating a flow. For Appium use the active driver's supported element actions, screenshot and navigation APIs; inspect that driver's capabilities rather than inventing cross-platform extensions. Check whether framework hooks capture automatically when screenshots=off.

On a macOS host with Xcode Simulator, `xcrun simctl list devices` identifies devices; permitted capture can use `xcrun simctl io DEVICE_UDID screenshot PATH`. Use existing UI automation for taps/typing. Simulator control alone is not a universal UI tapping interface; Windows has no local iOS Simulator. Browser history back, Android system Back and an iOS navigation control are different operations. Missing device/framework support leaves those checks untested while independent checks continue.

Reference entry points (checked 2026-10-19; command availability still depends on installed versions):
- https://playwright.dev/docs/input
- https://developer.android.com/tools/adb
- https://docs.maestro.dev/ (consult installed command reference if online reference is unavailable)
- https://appium.io/docs/en/latest/intro/drivers/
- https://developer.apple.com/documentation/xcode/running-your-app-in-simulator-or-on-a-device

These are adapters, not claims that the commands were exercised on a real device in this skill release. Capture and image-review lifecycle is defined in [Screenshot evidence](screenshots.md).
