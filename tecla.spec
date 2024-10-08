#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v20
# autospec commit: f35655a
#
Name     : tecla
Version  : 47.0
Release  : 4
URL      : https://gitlab.gnome.org/GNOME/tecla/-/archive/47.0/tecla-47.0.tar.gz
Source0  : https://gitlab.gnome.org/GNOME/tecla/-/archive/47.0/tecla-47.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: tecla-bin = %{version}-%{release}
Requires: tecla-data = %{version}-%{release}
Requires: tecla-license = %{version}-%{release}
Requires: tecla-locales = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : pkgconfig(libadwaita-1)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Tecla
Tecla is a keyboard layout viewer.
Tecla uses GTK/Libadwaita for UI, and libxkbcommon to deal with keyboard maps.

%package bin
Summary: bin components for the tecla package.
Group: Binaries
Requires: tecla-data = %{version}-%{release}
Requires: tecla-license = %{version}-%{release}

%description bin
bin components for the tecla package.


%package data
Summary: data components for the tecla package.
Group: Data

%description data
data components for the tecla package.


%package dev
Summary: dev components for the tecla package.
Group: Development
Requires: tecla-bin = %{version}-%{release}
Requires: tecla-data = %{version}-%{release}
Provides: tecla-devel = %{version}-%{release}
Requires: tecla = %{version}-%{release}

%description dev
dev components for the tecla package.


%package license
Summary: license components for the tecla package.
Group: Default

%description license
license components for the tecla package.


%package locales
Summary: locales components for the tecla package.
Group: Default

%description locales
locales components for the tecla package.


%prep
%setup -q -n tecla-47.0
cd %{_builddir}/tecla-47.0
pushd ..
cp -a tecla-47.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1727476928
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/tecla
cp %{_builddir}/tecla-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/tecla/13d2034b5ee3cb8d1a076370cf8f0e344a5d0855 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang tecla
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/tecla
/usr/bin/tecla

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.gnome.Tecla.desktop
/usr/share/icons/hicolor/scalable/apps/org.gnome.Tecla.svg
/usr/share/icons/hicolor/symbolic/apps/org.gnome.Tecla-symbolic.svg

%files dev
%defattr(-,root,root,-)
/usr/share/pkgconfig/tecla.pc

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tecla/13d2034b5ee3cb8d1a076370cf8f0e344a5d0855

%files locales -f tecla.lang
%defattr(-,root,root,-)

