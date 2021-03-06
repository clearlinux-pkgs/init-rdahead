#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : init-rdahead
Version  : 24
Release  : 32
URL      : http://localhost/cgit/projects/init-rdahead/snapshot/init-rdahead-24.tar.gz
Source0  : http://localhost/cgit/projects/init-rdahead/snapshot/init-rdahead-24.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: init-rdahead-bin = %{version}-%{release}
Requires: init-rdahead-license = %{version}-%{release}

%description
Read ahead boot files in hyper-v, AWS and desktop.
To build in debug mode:
make DEBUG=1

%package bin
Summary: bin components for the init-rdahead package.
Group: Binaries
Requires: init-rdahead-license = %{version}-%{release}

%description bin
bin components for the init-rdahead package.


%package extras
Summary: extras components for the init-rdahead package.
Group: Default

%description extras
extras components for the init-rdahead package.


%package license
Summary: license components for the init-rdahead package.
Group: Default

%description license
license components for the init-rdahead package.


%prep
%setup -q -n init-rdahead-24
cd %{_builddir}/init-rdahead-24

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604097278
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1604097278
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/init-rdahead
cp %{_builddir}/init-rdahead-24/LICENSE %{buildroot}/usr/share/package-licenses/init-rdahead/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/initra
/usr/bin/initra-aws

%files extras
%defattr(-,root,root,-)
/usr/bin/initra-desktop

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/init-rdahead/8624bcdae55baeef00cd11d5dfcfa60f68710a02
