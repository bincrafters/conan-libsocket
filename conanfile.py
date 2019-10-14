from conans import ConanFile, CMake, tools
import os


class libsocket(ConanFile):
    name = "libsocket"
    description = "Socket library with support for TCP, UDP and Unix sockets"
    topics = ("conan", "libsocket", "socket", "sockets")
    url = "https://github.com/bincrafters/conan-libsocket"
    homepage = "https://github.com/dermesser/libsocket"
    license = "https://github.com/dermesser/libsocket/blob/master/LICENSE"
    author = "Emanuel Bennici <benniciemanuel78@gmail.com>"

    exports_sources = ["CMakeLists.txt"]
    generators = "cmake"

    settings = "os", "arch", "compiler", "build_type"
    options = {
        "shared":       [True, False],
        "fPIC":         [True, False],
        "out_":         ['all', 'cpp', 'c']
    }

    default_options = {'shared': False, 'fPIC': True, 'out_': 'all'}

    _source_subfolder = "source_subfolder"
    _build_subfolder = "build_subfolder"

    def source(self):
        tools.get(**self.conan_data["sources"][self.version])
        extracted_dir = self.name + "-" + self.version
        os.rename(extracted_dir, self._source_subfolder)


    def _configure_cmake(self):
        cmake = CMake(self)
        cmake.definitions["BUILD_STATIC_LIBS"] = not self.options.shared
        cmake.definitions["BUILD_SHARED_LIBS"] = self.options.shared
        cmake.configure(build_folder=self._build_subfolder)

        return cmake


    def build(self):
        if not self.options.shared:
            tools.replace_in_file(os.path.join(self._source_subfolder, 'CMakeLists.txt'),
                                  'ADD_DEPENDENCIES(socket++ socket)',
                                  'ADD_DEPENDENCIES(socket++_int socket)')
            tools.replace_in_file(os.path.join(self._source_subfolder, 'CMakeLists.txt'),
                                  'export(TARGETS socket++ socket_int',
                                  'export(TARGETS socket++_int socket_int')
        tools.replace_in_file(os.path.join(self._source_subfolder, 'C++', 'CMakeLists.txt'),
                              'SET(CMAKE_CXX_FLAGS "-std=c++11") # -DVERBOSE")',
                              'SET(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11") # -DVERBOSE")')

        cmake = self._configure_cmake()
        cmake.build()


    def package(self):
        cmake = self._configure_cmake()
        cmake.install()

        # copy LICENSE File
        self.copy(pattern="LICENSE", dst="licenses", src=self._source_subfolder)


    def package_info(self):
        self.cpp_info.libs = ["socket++", "socket"]
