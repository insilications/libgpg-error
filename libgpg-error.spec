#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x249B39D24F25E3B6
#
%define keepstatic 1
Name     : libgpg-error
Version  : 1.33
Release  : 31
URL      : ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-1.33.tar.gz
Source0  : ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-1.33.tar.gz
Source99 : ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-1.33.tar.gz.sig
Summary  : libgpg-error
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0+ LGPL-2.1
Requires: libgpg-error-bin = %{version}-%{release}
Requires: libgpg-error-data = %{version}-%{release}
Requires: libgpg-error-lib = %{version}-%{release}
Requires: libgpg-error-license = %{version}-%{release}
Requires: libgpg-error-locales = %{version}-%{release}
Requires: libgpg-error-man = %{version}-%{release}
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32

%description
This is a library that defines common error values for all GnuPG
components.  Among these are GPG, GPGSM, GPGME, GPG-Agent, libgcrypt,
pinentry, SmartCard Daemon and possibly more in the future.

%package bin
Summary: bin components for the libgpg-error package.
Group: Binaries
Requires: libgpg-error-data = %{version}-%{release}
Requires: libgpg-error-license = %{version}-%{release}
Requires: libgpg-error-man = %{version}-%{release}

%description bin
bin components for the libgpg-error package.


%package data
Summary: data components for the libgpg-error package.
Group: Data

%description data
data components for the libgpg-error package.


%package dev
Summary: dev components for the libgpg-error package.
Group: Development
Requires: libgpg-error-lib = %{version}-%{release}
Requires: libgpg-error-bin = %{version}-%{release}
Requires: libgpg-error-data = %{version}-%{release}
Provides: libgpg-error-devel = %{version}-%{release}

%description dev
dev components for the libgpg-error package.


%package dev32
Summary: dev32 components for the libgpg-error package.
Group: Default
Requires: libgpg-error-lib32 = %{version}-%{release}
Requires: libgpg-error-bin = %{version}-%{release}
Requires: libgpg-error-data = %{version}-%{release}
Requires: libgpg-error-dev = %{version}-%{release}

%description dev32
dev32 components for the libgpg-error package.


%package doc
Summary: doc components for the libgpg-error package.
Group: Documentation
Requires: libgpg-error-man = %{version}-%{release}

%description doc
doc components for the libgpg-error package.


%package extras
Summary: extras components for the libgpg-error package.
Group: Default

%description extras
extras components for the libgpg-error package.


%package lib
Summary: lib components for the libgpg-error package.
Group: Libraries
Requires: libgpg-error-data = %{version}-%{release}
Requires: libgpg-error-license = %{version}-%{release}

%description lib
lib components for the libgpg-error package.


%package lib32
Summary: lib32 components for the libgpg-error package.
Group: Default
Requires: libgpg-error-data = %{version}-%{release}
Requires: libgpg-error-license = %{version}-%{release}

%description lib32
lib32 components for the libgpg-error package.


%package license
Summary: license components for the libgpg-error package.
Group: Default

%description license
license components for the libgpg-error package.


%package locales
Summary: locales components for the libgpg-error package.
Group: Default

%description locales
locales components for the libgpg-error package.


%package man
Summary: man components for the libgpg-error package.
Group: Default

%description man
man components for the libgpg-error package.


%prep
%setup -q -n libgpg-error-1.33
pushd ..
cp -a libgpg-error-1.33 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1546529996
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -ffat-lto-objects -ffunction-sections -flto=4 -fno-semantic-interposition "
%configure
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export ASFLAGS="$ASFLAGS --32"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure     --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../build32;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1546529996
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libgpg-error
cp COPYING %{buildroot}/usr/share/package-licenses/libgpg-error/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/libgpg-error/COPYING.LIB
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install
%find_lang libgpg-error

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/gpg-error
/usr/bin/gpg-error-config
/usr/bin/gpgrt-config
/usr/bin/yat2m

%files data
%defattr(-,root,root,-)
%exclude /usr/share/common-lisp/source/gpg-error/gpg-error-codes.lisp
%exclude /usr/share/common-lisp/source/gpg-error/gpg-error-package.lisp
%exclude /usr/share/common-lisp/source/gpg-error/gpg-error.asd
%exclude /usr/share/common-lisp/source/gpg-error/gpg-error.lisp
/usr/share/libgpg-error/errorref.txt

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libgpg-error.so
/usr/lib64/pkgconfig/gpg-error.pc
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libgpg-error.so
/usr/lib32/pkgconfig/32gpg-error.pc
/usr/lib32/pkgconfig/gpg-error.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/info/*

%files extras
%defattr(-,root,root,-)
/usr/share/common-lisp/source/gpg-error/gpg-error-codes.lisp
/usr/share/common-lisp/source/gpg-error/gpg-error-package.lisp
/usr/share/common-lisp/source/gpg-error/gpg-error.asd
/usr/share/common-lisp/source/gpg-error/gpg-error.lisp

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgpg-error.so.0
/usr/lib64/libgpg-error.so.0.25.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libgpg-error.so.0
/usr/lib32/libgpg-error.so.0.25.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libgpg-error/COPYING
/usr/share/package-licenses/libgpg-error/COPYING.LIB

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/gpgrt-config.1

%files locales -f libgpg-error.lang
%defattr(-,root,root,-)

