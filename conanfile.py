#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import ConanFile, CMake, tools
import os


class libsocket(ConanFile):
    name = "libsocket"
    version = "2.4.1"
    description = "Conan.io Package for libsocket Libary."
    url = "https://github.com/bintray/conan-libsocket"
    homepage = "https://github.com/dermesser/libsocket"
    author = "Emanuel Bennici <benniciemanuel78@gmail.com>"
    license = "https://github.com/dermesser/libsocket/blob/master/LICENSE"

    exports = ["LICENSE"]

    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    #settings = {"os": ["Linux"], "arch": None, "compiler": None, "build_type": None}
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


    def source(self):
        self.run("git clone https://github.com/dermesser/libsocket --depth 1 %s" % self.source_subfolder)


    def configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_STATIC_LIBS"] = not self.options.shared
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.configure(build_folder=self.build_subfolder)

        return cmake


    def build(self):
        if not self.options.shared:
            tools.replace_in_file(os.path.join(self.source_subfolder, 'CMakeLists.txt'),
                                  'ADD_DEPENDENCIES(socket++ socket)',
                                  'ADD_DEPENDENCIES(socket++_int socket)')
            tools.replace_in_file(os.path.join(self.source_subfolder, 'CMakeLists.txt'),
                                  'export(TARGETS socket++ socket_int',
                                  'export(TARGETS socket++_int socket_int')
        tools.replace_in_file(os.path.join(self.source_subfolder, 'C++', 'CMakeLists.txt'),
                              'SET(CMAKE_CXX_FLAGS "-std=c++11") # -DVERBOSE")',
                              'SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11") # -DVERBOSE")')

        cmake = self.configure_cmake()
        cmake.build()


    def package(self):
        cmake = self.configure_cmake()
        cmake.install()

        # copy LICENSE File
        self.copy(pattern="LICENSE", dst="licenses", src=self.source_subfolder)


    def package_info(self):
        self.cpp_info.libs = ["socket++", "socket"]


    def config_options(self):
        if platform.system() != "Linux":
            raise Exception("Unsupported System! This package currently only support Linux")
