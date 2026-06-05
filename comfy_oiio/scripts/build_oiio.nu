let oiio_root = (git grab https://github.com/AcademySoftwareFoundation/OpenImageIO)
let reset = false
# let root = ($env.PWD)
let root = $oiio_root

$env.config.rm.always_trash = false

if $reset {
    rm -rf build
}
# let build_root = ($root | path join build_root)
let build_root = get-build-root openimageio 
# let build_env = {
#     ZLIB_ROOT : ($build_root | path join zlib build)
#     TIFF_ROOT : ($build_root | path join libTiff)
#     OpenEXR_ROOT : ($build_root | path join openexr dist)
#     Imath_DIR: ($build_root | path join openexr dist lib cmake Imath)
#     Imath_INCLUDE_DIR: ($build_root | path join openexr dist include Imath)
#     Imath_LIBRARY: ($build_root | path join openexr dist lib Imath-3_2.lib)
#     JPEG_ROOT : ($build_root | path join libjpeg-turbo build)
# }
mkdir $build_root

# NOTE: install zlib
cd $build_root
clone-or-update "./zlib" https://github.com/madler/zlib
cd zlib

if $reset {
    rm -rf build
}

cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=.
cmake --build build --config Release --target install
# rm build/Release/zlib.lib

#
# if not ("./zlib" | path exists) {
#     git clone https://github.com/madler/zlib
# }
# cd zlib
# git fetch
# git pull

# NOTE: Install libTiff
cd $build_root
clone-or-update "./libtiff"  https://gitlab.com/libtiff/libtiff.git
cd libtiff
if $reset {
    try {
        rm -rf build
        git reset --hard HEAD
    } catch {
        print "Nothing to clean for libtiff"
    }
}
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DBUILD_SHARED_LIBS=OFF -DCMAKE_INSTALL_PREFIX=.
cmake --build build --config Release --target install

# NOTE: install libjpeg-turbo
cd $build_root
clone-or-update "./libjpeg-turbo" https://github.com/libjpeg-turbo/libjpeg-turbo  
cd libjpeg-turbo
if $reset {
    rm -rf build
}
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DENABLE_SHARED=OFF -DCMAKE_INSTALL_PREFIX=.
cmake --build build --config Release --target install 

# NOTE: install openexr
cd $build_root
clone-or-update "./openexr" https://github.com/AcademySoftwareFoundation/openexr
cd openexr
if $reset {
    rm -rf build
}
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=dist -DBUILD_TESTING=OFF -DBUILD_SHARED_LIBS=OFF -DOPENEXR_BUILD_TOOLS=OFF -DOPENEXR_INSTALL_TOOLS=OFF -DOPENEXR_INSTALL_EXAMPLES=OFF -DZLIB_ROOT=($build_root | path join zlib)
cmake --build build --target install --config Release
let imath_lib = (glob dist/lib/Imath*.lib | get -i 0)

# NOTE: install pybind
cd $build_root 
clone-or-update "./pybind11" https://github.com/pybind/pybind11
cd pybind11
cmake -S . -B build -DCMAKE_BUILD_TYPE=Release -DENABLE_SHARED=OFF -DPYBIND11_TEST=OFF -DCMAKE_INSTALL_PREFIX=.
cmake --build build --config Release --target install 


# NOTE: install open image io
cd $root
cmake -S . -B build -DVERBOSE=ON -DCMAKE_BUILD_TYPE=Release -DOIIO_BUILD_TESTS=OFF -DUSE_PYTHON=1 -DUSE_QT=0 -DBUILD_SHARED_LIBS=0 -DLINKSTATIC=1  $"-DZLIB_ROOT=($build_root | path join zlib)" $"-Dpybind11_ROOT=($build_root | path join pybind11)" $"-DTIFF_ROOT=($build_root | path join libTiff)" $"-DOpenEXR_ROOT=($build_root | path join openexr dist)" $"-DImath_DIR=($build_root | path join openexr dist lib cmake Imath)" $"-DImath_INCLUDE_DIR=($build_root | path join openexr dist include Imath)" $"-DImath_LIBRARY=($imath_lib)" $"-DJPEG_ROOT=($build_root | path join libjpeg-turbo)" $"-Dlibjpeg-turbo_ROOT=($build_root | path join libjpeg-turbo)"
cmake --build build --target install --config Release

