import unittest
from pathlib import Path
from unittest.mock import patch

from undetected_geckodriver import utils
from undetected_geckodriver.driver import Firefox


class PlatformSupportTests(unittest.TestCase):
    def test_supported_platforms_present(self):
        self.assertIn("Linux", utils.PLATFORM_DEPENDENT_PARAMS)
        self.assertIn("Windows", utils.PLATFORM_DEPENDENT_PARAMS)
        self.assertIn("Darwin", utils.PLATFORM_DEPENDENT_PARAMS)

    @patch("undetected_geckodriver.utils.platform.system", return_value="Windows")
    def test_windows_cache_path_uses_home_directory(self, _):
        with patch("pathlib.Path.home", return_value=Path("C:/Users/Test")):
            cache_path = utils.get_platform_cache_path()
        self.assertEqual(
            cache_path.replace("\\", "/"),
            "C:/Users/Test/AppData/Local/undetected_firefox",
        )

    @patch("undetected_geckodriver.utils.platform.system", return_value="Darwin")
    def test_mac_cache_path_uses_home_directory(self, _):
        with patch("pathlib.Path.home", return_value=Path("/Users/test")):
            cache_path = utils.get_platform_cache_path()
        self.assertEqual(cache_path, "/Users/test/Library/Caches/undetected_firefox")

    def test_darwin_paths_use_contents_layout(self):
        darwin = utils.PLATFORM_DEPENDENT_PARAMS["Darwin"]
        self.assertIn("Resources/libxul.dylib", darwin["xul"])
        self.assertIn("MacOS/firefox", darwin["firefox_execs"])

    def test_resolve_installation_path_prefers_valid_parent(self):
        driver = object.__new__(Firefox)
        driver._platform_dependent_params = {"xul": "Resources/libxul.dylib"}

        with patch("os.path.exists") as exists:
            exists.side_effect = lambda p: p.endswith("/Contents/Resources/libxul.dylib")
            resolved = driver._resolve_installation_path_from_binary(
                "/Applications/Firefox.app/Contents/MacOS"
            )

        self.assertEqual(resolved, "/Applications/Firefox.app/Contents")


if __name__ == "__main__":
    unittest.main()
