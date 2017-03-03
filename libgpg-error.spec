#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x249B39D24F25E3B6 (dshaw@jabberwocky.com)
#
Name     : libgpg-error
Version  : 1.27
Release  : 21
URL      : ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-1.27.tar.bz2
Source0  : ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-1.27.tar.bz2
Source99 : ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-1.27.tar.bz2.sig
Summary  : libgpg-error
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0+ LGPL-2.1
Requires: libgpg-error-bin
Requires: libgpg-error-lib
Requires: libgpg-error-data
Requires: libgpg-error-doc
Requires: libgpg-error-locales
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
Requires: libgpg-error-data

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
Requires: libgpg-error-lib
Requires: libgpg-error-bin
Requires: libgpg-error-data
Provides: libgpg-error-devel

%description dev
dev components for the libgpg-error package.


%package dev32
Summary: dev32 components for the libgpg-error package.
Group: Default
Requires: libgpg-error-lib32
Requires: libgpg-error-bin
Requires: libgpg-error-data
Requires: libgpg-error-dev

%description dev32
dev32 components for the libgpg-error package.


%package doc
Summary: doc components for the libgpg-error package.
Group: Documentation

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
Requires: libgpg-error-data

%description lib
lib components for the libgpg-error package.


%package lib32
Summary: lib32 components for the libgpg-error package.
Group: Default
Requires: libgpg-error-data

%description lib32
lib32 components for the libgpg-error package.


%package locales
Summary: locales components for the libgpg-error package.
Group: Default

%description locales
locales components for the libgpg-error package.


%prep
%setup -q -n libgpg-error-1.27
pushd ..
cp -a libgpg-error-1.27 build32
popd

%build
export LANG=C
export SOURCE_DATE_EPOCH=1488574027
export CFLAGS="$CFLAGS -Os -ffunction-sections "
export FCFLAGS="$CFLAGS -Os -ffunction-sections "
export FFLAGS="$CFLAGS -Os -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1488574027
rm -rf %{buildroot}
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
/usr/share/aclocal/*.m4

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libgpg-error.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*

%files extras
%defattr(-,root,root,-)
/usr/share/common-lisp/source/gpg-error/gpg-error-codes.lisp
/usr/share/common-lisp/source/gpg-error/gpg-error-package.lisp
/usr/share/common-lisp/source/gpg-error/gpg-error.asd
/usr/share/common-lisp/source/gpg-error/gpg-error.lisp

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgpg-error.so.0
/usr/lib64/libgpg-error.so.0.22.0

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libgpg-error.so.0
/usr/lib32/libgpg-error.so.0.22.0

%files locales -f libgpg-error.lang
%defattr(-,root,root,-)

