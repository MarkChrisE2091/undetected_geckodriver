# Constants #
TO_REPLACE_STRING = b"webdriver"

PLATFORM_DEPENDENT_PARAMS = {
    "Windows": {
        "firefox_execs": ["firefox.exe"],
        "firefox_paths": [
            "C:\\Program Files\\Mozilla Firefox",
            "C:\\Program Files (x86)\\Mozilla Firefox",
        ],
        "undetected_path": "AppData/Local/undetected_firefox",
        "xul": "xul.dll",
    },
    "Darwin": {
        "firefox_execs": ["MacOS/firefox", "MacOS/firefox-bin"],
        "firefox_paths": [
            "/Applications/Firefox.app/Contents",
            "/Applications/Firefox Developer Edition.app/Contents",
            "/Applications/Firefox Nightly.app/Contents",
        ],
        "undetected_path": "Library/Caches/undetected_firefox",
        "xul": "Resources/libxul.dylib",
    },
    "Linux": {
        "firefox_execs": ["firefox", "firefox-bin"],
        "firefox_paths": [
            "/usr/lib/firefox",
            "/usr/lib/firefox-esr",
            "/usr/lib/firefox-developer-edition",
            "/usr/lib/firefox-nightly",
            "/usr/lib/firefox-trunk",
            "/usr/lib/firefox-beta",
        ],
        "undetected_path": ".cache/undetected_firefox",
        "xul": "libxul.so",
    },
}
