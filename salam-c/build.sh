#!/bin/bash

rm -fr build
mkdir build

cmake -B ./build

cmake --build ./build

os=$(uname)

# Check if the OS is not Darwin
if [ "$os" != "Darwin" ]; then
    mkdir snapcraft-build
    mv build/salam-c snapcraft-build
    cp snapcraft-dump.yaml snapcraft-build/snapcraft.yaml
    cd snapcraft-build
    snapcraft
    snapcraft upload  salam-c_*_amd64.snap
else
    echo -e "\nMacOS is detected...\n"
fi

rm -fr build
rm -fr snapcraft-build
