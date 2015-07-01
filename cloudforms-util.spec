Name:		cloudforms-util
Version:	0.2
Release:	1
Summary:	Utilities for CloudForms

Group:		Cloud Management Tools
License:	GPLv3+
URL:		https://github.com/georgegoh/%{name}
Source0:	https://github.com/georgegoh/%{name}/archive/%{version}.tar.gz

BuildArch:	noarch
Packager:	George Goh <george.goh@redhat.com>

%description
Aliases and environment settings to make working with CloudForms on the command line easier.

%prep

%build

%install
mkdir -p "%{buildroot}/etc/profile.d"
mkdir "%{buildroot}/root"
cd %{_builddir}/%{name}-%{version}
install --backup --mode=0644 src/cloudforms-util.sh "%{buildroot}/etc/profile.d/cloudforms-util.sh"
install --backup --mode=0644 src/irbrc "%{buildroot}/root/.irbrc"
install --backup --mode=0644 src/irbrc_rails "%{buildroot}/root/.irbrc_rails"

%files
%doc
/etc/profile.d/cloudforms-util.sh
/root/.irbrc
/root/.irbrc_rails

%post
echo "Shortcut aliases for CloudForms:" >> /etc/motd
echo "  cf    - bring up the rails console with $evm object loaded." >> /etc/motd
echo "  auto  - tail -f automate.log" >> /etc/motd
echo "  evm   - tail -f evm.log" >> /etc/motd
echo "  log   - cd /var/www/miq/vmdb/log" >> /etc/motd
echo "  scrub - truncate the automate and evm logs." >> /etc/motd

%changelog

