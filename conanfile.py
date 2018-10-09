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

    settings = {"os": ["Linux"], "arch": None, "compiler": None, "build_type": None}
    options = dict({
        "shared":       [True, False],
        "fPIC":         [True, False],
        "out_":         ['all', 'cpp', 'c']
    })

    default_options = "shared=False", "fPIC=True", "out_=all"
    build_policy = "missing"

    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def source(self):
        self.run("git clone https://github.com/dermesser/libsocket %s" % self.source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_STATIC_LIBS"] = not self.options.shared
        if self.options.fPIC:
            cmake.definitions["CMAKE_CXX_FLAGS"] = "-fPIC -Iheaders/"

        return cmake

    def build(self):
        cmake = self.configure_cmake()

        make_args = ('socket_int socket++_int' if not self.options.shared else '')

        self.run("cd %s && cmake CMakeLists.txt %s" % (self.source_subfolder, cmake.command_line))
        self.run("cd %s && make %s" % (self.source_subfolder, make_args))


    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        self.copy("*.h", dst="include/libsocket", src=self.source_subfolder + "/headers")
        self.copy("*.hpp", dst="include/libsocket", src=self.source_subfolder + "/headers")
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["socket++", "socket"]

