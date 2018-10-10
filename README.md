## Package Status

| Bintray   | Linux Build |
| :--------:|:-----------------:|
| [ ![Download](https://api.bintray.com/packages/l0nax/stable/libsocket%3Al0nax/images/download.svg) ](https://bintray.com/l0nax/stable/libsocket%3Al0nax/_latestVersion) | [![Build Status](https://travis-ci.org/bincrafters/conan-libsocket.svg?branch=testing%2F2.4.1)](https://travis-ci.org/bincrafters/conan-libsocket) |

## Conan.io Information

Bincrafters packages can be found in the following public Conan repository:

[Bincrafters Public Conan Repository on Bintray](https://bintray.com/bincrafters/public-conan)

*Note: You can click the "Set Me Up" button on the Bintray page above for instructions on using packages from this repository.*

## Setup

To configure your Conan Client to work with Arsen packages, you will need to add
the Bincrafter Repository to the list of Remotes.
```bash
$ conan remote add bincrafter-public https://api.bintray.com/conan/bincrafters/public-conan
```

## Project Setup

Here is a Example _conanfile.txt_:
```
[requires]
libsocket/2.4.1@bincrafters/stable

[generators]
cmake
```

Complete the installation of requirements for your project running:
```
$ conan install . --build=missing
```

## Options

Here is a List off all possible Options that you can use:

| Option    | Description                               | Default | Possible Values |
| --------- | ----------------------------------------- | ------- | --------------- |
| shared    | Build the shared library                  | False   | True, False     |
| fPIC      | Compile the Library with the '-fPIC' Flag | True    | True, False     |

## Issues

If you wish to report an issue or make a request for a Bincrafters package, please do so here:

[Bincrafters Community Issues](https://github.com/bincrafters/community/issues)

## General Information

This GIT repository is managed by the Bincrafters team and holds files related to Conan.io.  For detailed information about Bincrafters and Conan.io, please visit the following resources:

[Bincrafters Wiki - Common README](https://github.com/bincrafters/community/wiki/Common-README.md)

[Bincrafters Technical Documentation](http://bincrafters.readthedocs.io/en/latest/)

[Bincrafters Blog](https://bincrafters.github.io)

## License Information

Bincrafters packages are hosted on [Bintray](https://bintray.com) and contain Open-Source software which is licensed by the software's maintainers and NOT Bincrafters.  For each Open-Source package published by Bincrafters, the packaging process obtains the required license files along with the original source files from the maintainer, and includes these license files in the generated Conan packages.

The contents of this GIT repository are completely separate from the software being packaged and therefore licensed separately.  The license for all files contained in this GIT repository are defined in the [LICENSE.md](LICENSE.md) file in this repository.  The licenses included with all Conan packages published by Bincrafters can be found in the Conan package directories in the following locations, relative to the Conan Cache root (`~/.conan` by default):

### License(s) for packaged software:

    ~/.conan/data/<pkg_name>/<pkg_version>/bincrafters/package/<random_package_id>/license/<LICENSE_FILES_HERE>

*Note :   The most common filenames for OSS licenses are `LICENSE` AND `COPYING` without file extensions.*

### License for Bincrafters recipe:

    ~/.conan/data/<pkg_name>/<pkg_version>/bincrafters/export/LICENSE.md

