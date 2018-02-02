#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : init-rdahead
Version  : 20
Release  : 25
URL      : http://localhost/cgit/projects/init-rdahead/snapshot/init-rdahead-20.tar.gz
Source0  : http://localhost/cgit/projects/init-rdahead/snapshot/init-rdahead-20.tar.gz
Source1  : initra.service
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: init-rdahead-bin
Requires: init-rdahead-config
BuildRequires : musl
BuildRequires : musl-dev
Patch1: fork-four.patch

%description
Read ahead boot files in hyper-v.
Smallest footprint is to  : make smallmusl
Make in debug mode        : make smallmusldebug
If you don't have gcc-musl: make small
If you don't want to strip: make initra

%package autostart
Summary: autostart components for the init-rdahead package.
Group: Default

%description autostart
autostart components for the init-rdahead package.


%package bin
Summary: bin components for the init-rdahead package.
Group: Binaries
Requires: init-rdahead-config

%description bin
bin components for the init-rdahead package.


%package config
Summary: config components for the init-rdahead package.
Group: Default

%description config
config components for the init-rdahead package.


%package extras
Summary: extras components for the init-rdahead package.
Group: Default

%description extras
extras components for the init-rdahead package.


%prep
%setup -q -n init-rdahead-20
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1511552603
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1511552603
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}/usr/lib/systemd/system
install -m 0644 %{SOURCE1} %{buildroot}/usr/lib/systemd/system/initra.service
## make_install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/
ln -s ../initra.service  %{buildroot}/usr/lib/systemd/system/multi-user.target.wants/initra.service
## make_install_append end

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/initra.service

%files bin
%defattr(-,root,root,-)
%exclude /usr/bin/initra-desktop
/usr/bin/initra
/usr/bin/initra-aws

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/initra.service
%exclude /usr/lib/systemd/system/multi-user.target.wants/initra.service

%files extras
%defattr(-,root,root,-)
/usr/bin/initra-desktop
/usr/lib/systemd/system/initra.service
/usr/lib/systemd/system/multi-user.target.wants/initra.service
