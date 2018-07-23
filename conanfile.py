#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class libsocket(ConanFile):
    name = "libsocket"
    version = "2.4.1"
    description = "Conan.io Package for libsocket Libary."
    url = "https://github.com/l0nax/conan-libsocket"
    homepage = "https://github.com/dermesser/libsocket"
    author = "Emanuel Bennici <benniciemanuel78@gmail.com>"
    license = "https://github.com/dermesser/libsocket/blob/master/LICENSE"

    exports = ["LICENSE"]

    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    settings = "os", "arch", "compiler", "build_type"
    options = dict({
        "shared":       [True, False],
        "only_cpp":     [True, False],
        "only_c":       [True, False],
        "fPIC":         [True, False],
    })

    default_options = "shared=False", "static=False", "fPIC=True"
    build_policy = "missing"

    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def config_options(self):
        if self.settings.os == 'Windows':
            raise Exception("This Libary does not support Windows!")
        if self.settings.os == 'MacOS':
            raise Exception("This Libary does not support Mac OS!")

        if self.settings.only_cpp && self.settings.only_c:
            raise Exception("Please choose if you would this Library with C++- or C-only Support.")

    def source(self):
        source_url = "https://github.com/dermesser/libsocket"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version

        os.rename(extracted_dir, self.source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_STATIC_LIB"] = (True if self.settings.static else False)
        if self.settings.fPIC:
            cmake.definitions["CMAKE_CXX_FLAGS"] = "-fPIC"

        cmake.configure(build_folder=self.build_subfolder)
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
