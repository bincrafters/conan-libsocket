#!/bin/bash

set -e
set -x

if [[ "$(uname -s)" == 'Darwin' ]]; then
    if which pyenv > /dev/null; then
        eval "$(pyenv init -)"
    fi
    pyenv activate conan
fi

python build.py

## Test the Package
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null && pwd )"
conan test ${DIR}/../_package-test ${CONAN_REFERENCE}@${CONAN_USERNAME}/${CONAN_CHANNEL}
