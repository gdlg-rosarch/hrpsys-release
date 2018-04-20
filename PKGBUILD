# Script generated with Bloom
pkgdesc="ROS - <p>An <a href="http://www.openrtm.org/pub/OpenRTM-aist/">OpenRTM-aist</a>-based robot controller. This package is the most tailored for humanoid (dual-arm and/or biped) robots for historical reason.</p> <p>hrpsys package does not only wraps but build and installs the code from its mainstream repository (<a href="https://github.com/fkanehiro/hrpsys-base/">github.com/fkanehiro/hrpsys-base</a>).</p> <p>The package version number is synchronized to that of mainstream, based on <a href="https://github.com/start-jsk/rtmros_common/issues/165#issuecomment-34536168">this decision</a>. Its semantics:<br/> <ul> <li><b>MAJOR</b>: Synchronized with <a href="http://wiki.ros.org/openhrp3">OpenHRP3</a></li> <li><b>MINOR</b>: Indicate IDL compatibility (packages with different version numbers in this section are NOT compatible)</li> <li><b>PATCH</b>: Packages with different version numbers in this section ARE compatible.</li> </ul> </p> <p>API document is <a href="http://fkanehiro.github.io/hrpsys-base/">auto-generated on github</a>. </p>"
url='http://ros.org/wiki/hrpsys'

pkgname='ros-kinetic-hrpsys'
pkgver='315.14.0_1'
pkgrel=1
arch=('any')
license=('EPL'
)

makedepends=('cmake'
'doxygen'
'freeglut'
'git'
'glew'
'graphviz'
'irrlicht'
'libxml2'
'libxmu'
'opencv'
'pkg-config'
'python2'
'qhull'
'ros-kinetic-mk'
'ros-kinetic-openhrp3'
'sdl'
'tk'
)

depends=('freeglut'
'irrlicht'
'libxml2'
'libxmu'
'opencv'
'python2'
'qhull'
'ros-kinetic-openhrp3'
'sdl'
'tk'
)

conflicts=()
replaces=()

_dir=hrpsys
source=()
md5sums=()

prepare() {
    cp -R $startdir/hrpsys $srcdir/hrpsys
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

