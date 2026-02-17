#!/bin/bash
set -e

ROOT=$(dirname $PWD)
rm -rf micropython-build
git clone https://github.com/micropython/micropython.git micropython-build
cd micropython-build
cd ports/unix
make submodules
make -j8
cd build-standard
cp micropython "$ROOT/bin/micropython"
chmod +x "$ROOT/bin/micropython"
rm -rf "$ROOT/micropython-build"