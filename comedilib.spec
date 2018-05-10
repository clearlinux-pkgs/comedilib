#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : comedilib
Version  : 0.11.0
Release  : 5
URL      : https://github.com/Linux-Comedi/comedilib/releases/download/r0_11_0/comedilib-0.11.0.tar.gz
Source0  : https://github.com/Linux-Comedi/comedilib/releases/download/r0_11_0/comedilib-0.11.0.tar.gz
Summary  : Data Acquisition library for the Comedi DAQ driver.
Group    : Development/Tools
License  : LGPL-2.1
Requires: comedilib-bin
Requires: comedilib-lib
Requires: comedilib-doc
Requires: comedilib-python3
Requires: comedilib-python
BuildRequires : bison
BuildRequires : flex
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : swig
BuildRequires : xmlto

%description
Comedilib is the library for the Comedi data acquisition driver
for Linux.  It allows Linux processes to acquire data from
supported DAQ cards, such as those from National Instruments.

%package bin
Summary: bin components for the comedilib package.
Group: Binaries

%description bin
bin components for the comedilib package.


%package dev
Summary: dev components for the comedilib package.
Group: Development
Requires: comedilib-lib
Requires: comedilib-bin
Provides: comedilib-devel

%description dev
dev components for the comedilib package.


%package doc
Summary: doc components for the comedilib package.
Group: Documentation

%description doc
doc components for the comedilib package.


%package lib
Summary: lib components for the comedilib package.
Group: Libraries

%description lib
lib components for the comedilib package.


%package python
Summary: python components for the comedilib package.
Group: Default
Requires: comedilib-python3

%description python
python components for the comedilib package.


%package python3
Summary: python3 components for the comedilib package.
Group: Default
Requires: python3-core

%description python3
python3 components for the comedilib package.


%prep
%setup -q -n comedilib-0.11.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1517619939
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1517619939
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/comedi_board_info
/usr/bin/comedi_config
/usr/bin/comedi_test

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/*.hpp
/usr/lib64/libcomedi.so
/usr/lib64/pkgconfig/comedilib.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/comedilib/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*
%doc /usr/share/man/man7/*
%doc /usr/share/man/man8/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcomedi.so.0
/usr/lib64/libcomedi.so.0.11.0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
