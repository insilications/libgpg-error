#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libgpg-error
Version  : 1.23
Release  : 15
URL      : ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-1.23.tar.bz2
Source0  : ftp://ftp.gnupg.org/gcrypt/libgpg-error/libgpg-error-1.23.tar.bz2
Summary  : libgpg-error
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.0+ LGPL-2.1
Requires: libgpg-error-bin
Requires: libgpg-error-lib
Requires: libgpg-error-data
Requires: libgpg-error-doc
Requires: libgpg-error-locales

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


%package locales
Summary: locales components for the libgpg-error package.
Group: Default

%description locales
locales components for the libgpg-error package.


%prep
%setup -q -n libgpg-error-1.23

%build
export LANG=C
export CFLAGS="$CFLAGS -Os -ffunction-sections "
export FCFLAGS="$CFLAGS -Os -ffunction-sections "
export FFLAGS="$CFLAGS -Os -ffunction-sections "
export CXXFLAGS="$CXXFLAGS -Os -ffunction-sections "
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
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

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so
/usr/share/aclocal/*.m4

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
/usr/lib64/*.so.*

%files locales -f libgpg-error.lang 
%defattr(-,root,root,-)

