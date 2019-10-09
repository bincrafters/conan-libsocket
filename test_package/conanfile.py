#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
from conans import ConanFile, CMake
import os, platform
import subprocess

class TestPackageConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def test(self):
        ## check if Binary can be executed
        p = subprocess.Popen("file " + os.path.join("bin", "test_package"), stdout=subprocess.PIPE, shell=True)
        output = str(p.communicate()[0])

        arch = platform.architecture()[0]

        ## only Execute if it's possible
        ## it's not releay a nice way..
        if arch == "64bit":
            if "64-bit" in output and "x86-64" in output:
                self.run(os.path.join("bin","test_package"), run_environment=True)
        elif arch == "32bit":
            if "32-bit" in output and "x86" in output:
                self.run(os.path.join("bin","test_package"), run_environment=True)
        else:
            self.output.warn("Could not run Test because Architecture does not match!")
