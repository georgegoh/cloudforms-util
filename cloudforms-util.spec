Name:      cloudforms-util
Version:   0.3
Release:   4
Summary:   Utilities for CloudForms

Group:     Applications/System
License:   GPLv3+
URL:       https://github.com/georgegoh/%{name}
Source0:   https://github.com/georgegoh/%{name}/archive/%{version}-%{release}.tar.gz

BuildArch: noarch

%description
Aliases and environment settings to make working with CloudForms on the command line easier.

%prep

%build

%install
mkdir -p "%{buildroot}/etc/profile.d"
mkdir "%{buildroot}/root"
cd %{_builddir}/%{name}-%{version}-%{release}
install --backup --mode=0644 src/cloudforms-util.sh "%{buildroot}/etc/profile.d/cloudforms-util.sh"
install --backup --mode=0644 src/irbrc "%{buildroot}/root/.irbrc"
install --backup --mode=0644 src/irbrc_rails "%{buildroot}/root/.irbrc_rails"

%files
%doc
/etc/profile.d/cloudforms-util.sh
/root/.irbrc
/root/.irbrc_rails

%post
cat > /etc/motd << 'EOF'
Shortcut aliases for CloudForms:
  cf    - bring up the rails console with $evm object loaded
  auto  - less +F automate.log
  evm   - less +F evm.log
  log   - cd /var/www/miq/vmdb/log
  scrub - truncate the automate and evm logs
  console - CloudForms appliance console
EOF

%changelog
* Mon Dec 21 2015 George Goh <george.goh@redhat.com> 0.3-4
- Updated profile.d script with the 'console' alias

* Tue Jul 14 2015 Eduardo Minguez <eminguez@redhat.com> 0.3-3
- Added appliance console

* Thu Jul 02 2015 Eduardo Minguez <eminguez@redhat.com> 0.3-2
- Changed tail -f by less +F

* Thu Jul 02 2015 George Goh <ggoh@redhat.com> 0.3-1
- Initial RPM release
