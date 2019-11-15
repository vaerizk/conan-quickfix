from conans import ConanFile, CMake, tools

import os

class QuickFIXConan(ConanFile):
    name = "quickfix"
    version="1.15.1"
    license = "The QuickFIX Software License"
    url = "https://github.com/vaerizk/conan-quickfix"
    homepage = "https://github.com/quickfix/quickfix"
    description = "C++ Fix Engine Library"
    topics = ("quickfix", "conan-recipe")

    settings = {
        "os": ["Windows"],
        "compiler": None,
        "build_type": None,
        "arch": None
    }
    options = {
        "shared": [False], # src\C++\CMakeLists.txt : 65
        "emx": [True, False],
        "ssl": [True, False]
    }
    default_options = {
        "shared": False,
        "emx": False,
        "ssl": False
    }

    revision_mode = "scm"

    generators = "cmake_paths"
    no_copy_source = True

    _source_subdir_name = "source_subdir"

    def configure(self):
        if self.options.ssl:
            self.options["openssl"].shared = True

    def build_requirements(self):
        self.build_requires("cmake_installer/[>3.0.0]@conan/stable")

    def requirements(self):
        if self.options.ssl:
            self.requires("openssl/1.1.1d", private=False)

    def source(self):
        url = "https://github.com/quickfix/quickfix/archive/v{}.zip".format(self.version)
        tools.get(url)
        os.rename("quickfix-{}".format(self.version), self._source_subdir_name)

    def build(self):
        cmake = CMake(self)
        cmake.definitions["CMAKE_TOOLCHAIN_FILE"] = os.path.join(self.build_folder, "conan_paths.cmake")
        cmake.definitions["HAVE_EMX"] = self.options.emx
        cmake.definitions["HAVE_SSL"] = self.options.ssl
        cmake.configure(source_folder=self._source_subdir_name)
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self._source_subdir_name)
        cmake.install()

    def package_info(self):
        self.cpp_info.includedirs = ["include"]
        if not self.options.ssl:
            self.cpp_info.system_libs = ["ws2_32"]
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.resdirs = ["share"]
