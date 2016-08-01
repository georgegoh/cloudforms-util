VERSION := 0.4
RELEASE := 1
BUILD_DIR := $(shell rpmbuild -E %{_builddir})/cloudforms-util-$(VERSION)-$(RELEASE)

rpm:
	mkdir -p $(BUILD_DIR)
	git archive $(VERSION)-$(RELEASE) | tar -x -C $(BUILD_DIR)
	rpmbuild -bb cloudforms-util.spec

install:
	install --backup --mode=0644 src/motd /etc/motd
	install --backup --mode=0644 src/cloudforms-util.sh /etc/profile.d/cloudforms-util.sh
	install --backup --mode=0644 src/irbrc /root/.irbrc
	install --backup --mode=0644 src/irbrc_rails /root/.irbrc_rails

