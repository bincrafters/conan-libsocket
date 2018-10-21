#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    if which pyenv > /dev/null; then
        eval "$(pyenv init -)"
    fi
    pyenv activate conan
fi

## create Environment Variables
export CONAN_UPLOAD="https://api.bintray.com/conan/bincrafters/public-conan"

## build Package
python build.py
