ROOT="$PWD"
rm -rf micropython-build
git clone https://github.com/micropython/micropython.git micropython-build
cd micropython-build
cd ports/unix
make submodules
make -j8
cd build-standard
install -D -m 755 micropython "$ROOT/bin/micropython"
rm -rf "$ROOT/micropython-build"