#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : keditbookmarks
Version  : 22.08.2
Release  : 44
URL      : https://download.kde.org/stable/release-service/22.08.2/src/keditbookmarks-22.08.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/22.08.2/src/keditbookmarks-22.08.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/22.08.2/src/keditbookmarks-22.08.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GFDL-1.2 GPL-2.0
Requires: keditbookmarks-bin = %{version}-%{release}
Requires: keditbookmarks-data = %{version}-%{release}
Requires: keditbookmarks-lib = %{version}-%{release}
Requires: keditbookmarks-license = %{version}-%{release}
Requires: keditbookmarks-locales = %{version}-%{release}
Requires: keditbookmarks-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kdoctools-dev
BuildRequires : qt6base-dev

%description
No detailed description available

%package bin
Summary: bin components for the keditbookmarks package.
Group: Binaries
Requires: keditbookmarks-data = %{version}-%{release}
Requires: keditbookmarks-license = %{version}-%{release}

%description bin
bin components for the keditbookmarks package.


%package data
Summary: data components for the keditbookmarks package.
Group: Data

%description data
data components for the keditbookmarks package.


%package dev
Summary: dev components for the keditbookmarks package.
Group: Development
Requires: keditbookmarks-lib = %{version}-%{release}
Requires: keditbookmarks-bin = %{version}-%{release}
Requires: keditbookmarks-data = %{version}-%{release}
Provides: keditbookmarks-devel = %{version}-%{release}
Requires: keditbookmarks = %{version}-%{release}

%description dev
dev components for the keditbookmarks package.


%package doc
Summary: doc components for the keditbookmarks package.
Group: Documentation
Requires: keditbookmarks-man = %{version}-%{release}

%description doc
doc components for the keditbookmarks package.


%package lib
Summary: lib components for the keditbookmarks package.
Group: Libraries
Requires: keditbookmarks-data = %{version}-%{release}
Requires: keditbookmarks-license = %{version}-%{release}

%description lib
lib components for the keditbookmarks package.


%package license
Summary: license components for the keditbookmarks package.
Group: Default

%description license
license components for the keditbookmarks package.


%package locales
Summary: locales components for the keditbookmarks package.
Group: Default

%description locales
locales components for the keditbookmarks package.


%package man
Summary: man components for the keditbookmarks package.
Group: Default

%description man
man components for the keditbookmarks package.


%prep
%setup -q -n keditbookmarks-22.08.2
cd %{_builddir}/keditbookmarks-22.08.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1665728498
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1665728498
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/keditbookmarks
cp %{_builddir}/keditbookmarks-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/keditbookmarks/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/keditbookmarks-%{version}/COPYING %{buildroot}/usr/share/package-licenses/keditbookmarks/7c203dee3a03037da436df03c4b25b659c073976 || :
cp %{_builddir}/keditbookmarks-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/keditbookmarks/bd75d59f9d7d9731bfabdc48ecd19e704d218e38 || :
pushd clr-build
%make_install
popd
%find_lang keditbookmarks

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/kbookmarkmerger
/usr/bin/keditbookmarks

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.keditbookmarks.desktop
/usr/share/config.kcfg/keditbookmarks.kcfg
/usr/share/qlogging-categories5/keditbookmarks.categories

%files dev
%defattr(-,root,root,-)
/usr/lib64/libkbookmarkmodel_private.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/keditbookmarks/index.cache.bz2
/usr/share/doc/HTML/ca/keditbookmarks/index.docbook
/usr/share/doc/HTML/de/keditbookmarks/index.cache.bz2
/usr/share/doc/HTML/de/keditbookmarks/index.docbook
/usr/share/doc/HTML/en/keditbookmarks/index.cache.bz2
/usr/share/doc/HTML/en/keditbookmarks/index.docbook
/usr/share/doc/HTML/es/keditbookmarks/index.cache.bz2
/usr/share/doc/HTML/es/keditbookmarks/index.docbook
/usr/share/doc/HTML/fr/keditbookmarks/index.cache.bz2
/usr/share/doc/HTML/fr/keditbookmarks/index.docbook
/usr/share/doc/HTML/it/keditbookmarks/index.cache.bz2
/usr/share/doc/HTML/it/keditbookmarks/index.docbook
/usr/share/doc/HTML/nl/keditbookmarks/index.cache.bz2
/usr/share/doc/HTML/nl/keditbookmarks/index.docbook
/usr/share/doc/HTML/pt/keditbookmarks/index.cache.bz2
/usr/share/doc/HTML/pt/keditbookmarks/index.docbook
/usr/share/doc/HTML/pt_BR/keditbookmarks/index.cache.bz2
/usr/share/doc/HTML/pt_BR/keditbookmarks/index.docbook
/usr/share/doc/HTML/ru/keditbookmarks/index.cache.bz2
/usr/share/doc/HTML/ru/keditbookmarks/index.docbook
/usr/share/doc/HTML/sv/keditbookmarks/index.cache.bz2
/usr/share/doc/HTML/sv/keditbookmarks/index.docbook
/usr/share/doc/HTML/uk/keditbookmarks/index.cache.bz2
/usr/share/doc/HTML/uk/keditbookmarks/index.docbook
/usr/share/doc/HTML/zh_CN/keditbookmarks/index.cache.bz2
/usr/share/doc/HTML/zh_CN/keditbookmarks/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkbookmarkmodel_private.so.5.97.0
/usr/lib64/libkbookmarkmodel_private.so.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/keditbookmarks/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/keditbookmarks/7c203dee3a03037da436df03c4b25b659c073976
/usr/share/package-licenses/keditbookmarks/bd75d59f9d7d9731bfabdc48ecd19e704d218e38

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/kbookmarkmerger.1
/usr/share/man/da/man1/kbookmarkmerger.1
/usr/share/man/de/man1/kbookmarkmerger.1
/usr/share/man/el/man1/kbookmarkmerger.1
/usr/share/man/es/man1/kbookmarkmerger.1
/usr/share/man/et/man1/kbookmarkmerger.1
/usr/share/man/fr/man1/kbookmarkmerger.1
/usr/share/man/it/man1/kbookmarkmerger.1
/usr/share/man/man1/kbookmarkmerger.1
/usr/share/man/nb/man1/kbookmarkmerger.1
/usr/share/man/nl/man1/kbookmarkmerger.1
/usr/share/man/pl/man1/kbookmarkmerger.1
/usr/share/man/pt/man1/kbookmarkmerger.1
/usr/share/man/pt_BR/man1/kbookmarkmerger.1
/usr/share/man/ru/man1/kbookmarkmerger.1
/usr/share/man/sr/man1/kbookmarkmerger.1
/usr/share/man/sv/man1/kbookmarkmerger.1
/usr/share/man/uk/man1/kbookmarkmerger.1
/usr/share/man/zh_CN/man1/kbookmarkmerger.1

%files locales -f keditbookmarks.lang
%defattr(-,root,root,-)

