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
        "fPIC":         [True, False],
        "out_":         ['all', 'cpp', 'c']
    })

    default_options = "shared=False", "fPIC=True", "out_=all"
    build_policy = "missing"

    source_subfolder = "source_subfolder"
    build_subfolder = "build_subfolder"

    def config_options(self):
        if self.settings.os == 'Windows':
            raise Exception("This Libary does not support Windows!")
        if self.settings.os == 'Macos':
            raise Exception("This Libary does not support Mac OS!")

    def source(self):
        source_url = "https://github.com/dermesser/libsocket"
        tools.get("{0}/archive/v{1}.tar.gz".format(source_url, self.version))
        extracted_dir = self.name + "-" + self.version

        os.rename(extracted_dir, self.source_subfolder)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_SHARED_LIB"] = (True if self.options["shared"] else False)
        if self.options.fPIC:
            cmake.definitions["CMAKE_CXX_FLAGS"] = "-fPIC -Iheaders/"

        return cmake

    def build(self):
        cmake = self.configure_cmake()
        self.run("cd %s && cmake CMakeLists.txt %s" % (self.source_subfolder, cmake.command_line))
        self.run("cd %s && cmake --build . %s" % (self.source_subfolder, cmake.build_config))

    def package(self):
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)
        cmake = self.configure_cmake()
        
        self.copy("*.h", dst="include", src=self.source_subfolder+"headers")
        self.copy("*.hpp", dst="include", src=self.source_subfolder+"headers")
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        if self.options.out_ == 'cpp':
            self.cpp_info.libs = ["socket++"]
        elif self.options.out_ == 'c':
            self.cpp_info.libs = ["socket"]
        else:
            self.cpp_info.libs = ["socket++", "socket"]
