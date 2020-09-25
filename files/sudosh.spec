Name:           sudosh
Version:        0.3.0
Release:        0
Summary:        Sudo Shell is a wrapper to run a login shell with sudo for the purpose of session audit logging.
Group:          Applications/System
License:        APACHE2
URL:            https://github.com/cloudposse/sudosh
Vendor:         Cloud Posse LLC
Source:         https://github.com/cloudposse/sudosh/archive/%{version}.tar.gz
Prefix:         %{_prefix}
Packager: 	    Jeffrey van Pelt
BuildRoot:      %{_tmppath}/%{name}-root

%description
The sudo command provides built-in session logging. Combined with sudoreplay it provides an easy way to review session logs on a bastion host. When used as a system login shell, it will force session logging.

%prep
%setup -q -n %{name}-%{version}

%build
make
make build

%undefine _missing_build_ids_terminate_build
%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
install release/sudosh-%{version} $RPM_BUILD_ROOT/usr/bin/sudosh

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/sudosh

%changelog
* Thu Sep 24 2020 Jeffrey van Pelt <jeff@vanpelt.one>
- Initial build
