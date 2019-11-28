from conans import ConanFile, CMake, tools

import os

class QuickFIXTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake_find_package"

    @property
    def _bin_dir(self):
        cmake = CMake(self)
        if cmake.is_multi_configuration:
            return str(self.settings.build_type)
        return "."

    def build_requirements(self):
        self.build_requires("cmake_installer/[>3.0.0]@conan/stable")

    def build(self):
        cmake = CMake(self)
        # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is
        # in "test_package"
        cmake.definitions["HAVE_SSL"] = self.options["quickfix"].ssl
        cmake.configure()
        cmake.build()

    def imports(self):
        self.copy("FIX42.xml", dst=self._bin_dir, src=os.path.dirname(os.path.realpath(__file__)))
        self.copy("tradeclient.cfg", dst=self._bin_dir, src=os.path.dirname(os.path.realpath(__file__)))

    def test(self):
        if not tools.cross_building(self.settings):
            self.run("example", cwd=self._bin_dir, run_environment=True)
