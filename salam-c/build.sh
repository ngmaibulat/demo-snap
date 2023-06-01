#!/bin/bash

rm -fr build
mkdir build
cd build

cmake ..

make


os=$(uname)

# Check if the OS is not Darwin
if [ "$os" != "Darwin" ]; then
    snapcraft
else
    echo "MacOS is detected..."
fi
