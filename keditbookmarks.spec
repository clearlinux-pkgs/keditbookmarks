#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v16
# autospec commit: b858a2a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : keditbookmarks
Version  : 24.05.2
Release  : 69
URL      : https://download.kde.org/stable/release-service/24.05.2/src/keditbookmarks-24.05.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.05.2/src/keditbookmarks-24.05.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.05.2/src/keditbookmarks-24.05.2.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
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
BuildRequires : gnupg
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86vm-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n keditbookmarks-24.05.2
cd %{_builddir}/keditbookmarks-24.05.2
pushd ..
cp -a keditbookmarks-24.05.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1720598328
mkdir -p clr-build
pushd clr-build
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
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

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
export SOURCE_DATE_EPOCH=1720598328
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/keditbookmarks
cp %{_builddir}/keditbookmarks-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/keditbookmarks/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/keditbookmarks-%{version}/COPYING %{buildroot}/usr/share/package-licenses/keditbookmarks/7c203dee3a03037da436df03c4b25b659c073976 || :
cp %{_builddir}/keditbookmarks-%{version}/COPYING.DOC %{buildroot}/usr/share/package-licenses/keditbookmarks/bd75d59f9d7d9731bfabdc48ecd19e704d218e38 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang keditbookmarks
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/kbookmarkmerger
/V3/usr/bin/keditbookmarks
/usr/bin/kbookmarkmerger
/usr/bin/keditbookmarks

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.keditbookmarks.desktop
/usr/share/config.kcfg/keditbookmarks.kcfg
/usr/share/qlogging-categories6/keditbookmarks.categories

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
/usr/share/doc/HTML/tr/keditbookmarks/index.cache.bz2
/usr/share/doc/HTML/tr/keditbookmarks/index.docbook
/usr/share/doc/HTML/uk/keditbookmarks/index.cache.bz2
/usr/share/doc/HTML/uk/keditbookmarks/index.docbook
/usr/share/doc/HTML/zh_CN/keditbookmarks/index.cache.bz2
/usr/share/doc/HTML/zh_CN/keditbookmarks/index.docbook

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libkbookmarkmodel_private.so.5.97.0
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
/usr/share/man/sr@latin/man1/kbookmarkmerger.1
/usr/share/man/sv/man1/kbookmarkmerger.1
/usr/share/man/tr/man1/kbookmarkmerger.1
/usr/share/man/uk/man1/kbookmarkmerger.1
/usr/share/man/zh_CN/man1/kbookmarkmerger.1

%files locales -f keditbookmarks.lang
%defattr(-,root,root,-)

