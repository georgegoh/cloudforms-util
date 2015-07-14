Name:      cloudforms-util
Version:   0.3
Release:   3
Summary:   Utilities for CloudForms

Group:     Applications/System
License:   GPLv3+
URL:       https://github.com/georgegoh/%{name}
Source0:   https://github.com/georgegoh/%{name}/archive/%{version}.tar.gz

BuildArch: noarch

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
echo "  cf    - bring up the rails console with $evm object loaded" >> /etc/motd
echo "  auto  - tail -f automate.log" >> /etc/motd
echo "  evm   - tail -f evm.log" >> /etc/motd
echo "  log   - cd /var/www/miq/vmdb/log" >> /etc/motd
echo "  scrub - truncate the automate and evm logs" >> /etc/motd
echo "  console - CloudForms appliance console" >> /etc/motd

%changelog
* Tue Jul 14 2015 Eduardo Minguez <eminguez@redhat.com> 0.3-3
- Added appliance console

* Thu Jul 02 2015 Eduardo Minguez <eminguez@redhat.com> 0.3-2
- Changed tail -f by less +F

* Thu Jul 02 2015 George Goh <ggoh@redhat.com> 0.3-1
- Initial RPM release
