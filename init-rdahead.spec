#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : init-rdahead
Version  : 22
Release  : 28
URL      : http://localhost/cgit/projects/init-rdahead/snapshot/init-rdahead-22.tar.gz
Source0  : http://localhost/cgit/projects/init-rdahead/snapshot/init-rdahead-22.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: init-rdahead-bin
Requires: init-rdahead-license

%description
Read ahead boot files in hyper-v, AWS and desktop.
To build in debug mode:
make DEBUG=1

%package bin
Summary: bin components for the init-rdahead package.
Group: Binaries
Requires: init-rdahead-license

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
%setup -q -n init-rdahead-22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534269428
make  %{?_smp_mflags} CFLAGS="-Os -g -fno-pic -feliminate-unused-debug-types -pipe -Wall -Wextra --param=ssp-buffer-size=32 -Wl,-z,now,-z,relro,-z,max-page-size=0x1000,-z,separate-code,--enable-new-dtags -Wp,-D_REENTRANT"

%install
export SOURCE_DATE_EPOCH=1534269428
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/init-rdahead
cp LICENSE %{buildroot}/usr/share/doc/init-rdahead/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/initra-desktop
/usr/bin/initra
/usr/bin/initra-aws

%files extras
%defattr(-,root,root,-)
/usr/bin/initra-desktop

%files license
%defattr(-,root,root,-)
/usr/share/doc/init-rdahead/LICENSE
