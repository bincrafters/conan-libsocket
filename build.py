#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cpt.packager import ConanMultiPackager

if __name__ == "__main__":
	builder = ConanMultiPackager();

	builder.add_common_builds()

        builder.add({'compiler.version': '7.3', 'arch': 'x86', 'build_type': 'Release', 'compiler': 'apple-clang'}, {"conan-libsocket:shared": True}))
        builder.add({'compiler.version': '7.3', 'arch': 'x86', 'build_type': 'Debug', 'compiler': 'apple-clang'}, {"conan-libsocket:shared": True}))
        builder.add({'compiler.version': '7.3', 'arch': 'x86_64', 'build_type': 'Release', 'compiler': 'apple-clang'}, {"conan-libsocket:shared": True}))
        builder.add({'compiler.version': '7.3', 'arch': 'x86_64', 'build_type': 'Debug', 'compiler': 'apple-clang'}, {"conan-libsocket:shared": True}))
        builder.add({'compiler.version': '8.0', 'arch': 'x86', 'build_type': 'Release', 'compiler': 'apple-clang'}, {"conan-libsocket:shared": True}))
        builder.add({'compiler.version': '8.0', 'arch': 'x86', 'build_type': 'Debug', 'compiler': 'apple-clang'}, {"conan-libsocket:shared": True}))
        builder.add({'compiler.version': '8.0', 'arch': 'x86_64', 'build_type': 'Release', 'compiler': 'apple-clang'}, {"conan-libsocket:shared": True}))
        builder.add({'compiler.version': '8.0', 'arch': 'x86_64', 'build_type': 'Debug', 'compiler': 'apple-clang'}, {"conan-libsocket:shared": True}))
        builder.add({'compiler.version': '8.1', 'arch': 'x86', 'build_type': 'Release', 'compiler': 'apple-clang'}, {"conan-libsocket:shared": True}))
        builder.add({'compiler.version': '8.1', 'arch': 'x86', 'build_type': 'Debug', 'compiler': 'apple-clang'}, {"conan-libsocket:shared": True}))
        builder.add({'compiler.version': '8.1', 'arch': 'x86_64', 'build_type': 'Release', 'compiler': 'apple-clang'}, {"conan-libsocket:shared": True}))
        builder.add({'compiler.version': '8.1', 'arch': 'x86_64', 'build_type': 'Debug', 'compiler': 'apple-clang'}, {"conan-libsocket:shared": True}))
        builder.add({'compiler.version': '7.3', 'arch': 'x86', 'build_type': 'Release', 'compiler': 'apple-clang'}))
        builder.add({'compiler.version': '7.3', 'arch': 'x86', 'build_type': 'Debug', 'compiler': 'apple-clang'}))
        builder.add({'compiler.version': '7.3', 'arch': 'x86_64', 'build_type': 'Release', 'compiler': 'apple-clang'}))
        builder.add({'compiler.version': '7.3', 'arch': 'x86_64', 'build_type': 'Debug', 'compiler': 'apple-clang'}))
        builder.add({'compiler.version': '8.0', 'arch': 'x86', 'build_type': 'Release', 'compiler': 'apple-clang'}))
        builder.add({'compiler.version': '8.0', 'arch': 'x86', 'build_type': 'Debug', 'compiler': 'apple-clang'}))
        builder.add({'compiler.version': '8.0', 'arch': 'x86_64', 'build_type': 'Release', 'compiler': 'apple-clang'}))
        builder.add({'compiler.version': '8.0', 'arch': 'x86_64', 'build_type': 'Debug', 'compiler': 'apple-clang'}))
        builder.add({'compiler.version': '8.1', 'arch': 'x86', 'build_type': 'Release', 'compiler': 'apple-clang'}))
        builder.add({'compiler.version': '8.1', 'arch': 'x86', 'build_type': 'Debug', 'compiler': 'apple-clang'}))
        builder.add({'compiler.version': '8.1', 'arch': 'x86_64', 'build_type': 'Release', 'compiler': 'apple-clang'}))
        builder.add({'compiler.version': '8.1', 'arch': 'x86_64', 'build_type': 'Debug', 'compiler': 'apple-clang'}))

	builder.run()
