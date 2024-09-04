%define debug_package %{nil}

Name:           percona-orchestrator
Version:        %{version}
Release:        3%{?dist}
Summary:        MySQL replication topology management and HA

Group:          Applications/Databases
License:        Apache 2.0
URL:            https://github.com/github/orchestrator
Source0:        %{name}-%{version}.tar.gz
Epoch:          2

BuildRequires:  gcc make perl-Digest-SHA
Requires:       jq >= 1.5
Requires:       oniguruma
Conflicts:      orchestrator

%description
MySQL replication topology management and HA

%package -n percona-orchestrator-cli
Group:          Applications/Databases
Summary:        MySQL replication topology management and HA
%description -n percona-orchestrator-cli
MySQL replication topology management and HA: binary only

%package -n percona-orchestrator-client
Group:          Applications/Databases
Summary:        MySQL replication topology management and HA
Requires:       jq >= 1.5
Requires:       curl
%description -n percona-orchestrator-client
MySQL replication topology management and HA: client script

%prep
%setup -q -n %{name}-%{version}


%build
bash script/build


%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 0644 etc/systemd/orchestrator.service %{buildroot}/lib/systemd/system/orchestrator.service
%{__install} -D -d -m 0755 %{buildroot}/usr/local/orchestrator/
%{__install} -D -d -m 0755 %{buildroot}/usr/bin/
%{__cp} -r bin/resources %{buildroot}/usr/local/orchestrator/resources
%{__rm} -rf %{buildroot}/usr/local/orchestrator/resources/bin
%{__cp}  bin/resources/bin/orchestrator-client %{buildroot}/usr/bin/
%{__cp}  bin/orchestrator %{buildroot}/usr/local/orchestrator/
%{__cp}  bin/orchestrator %{buildroot}/usr/bin/
%{__cp}  conf/orchestrator-sample* %{buildroot}/usr/local/orchestrator/

%files
%doc LICENSE
%config /lib/systemd/system/orchestrator.service
/usr/local/orchestrator/resources
%attr(755, root, root) /usr/local/orchestrator/orchestrator
/usr/local/orchestrator/orchestrator-sample.conf.json
/usr/local/orchestrator/orchestrator-sample-sqlite.conf.json

%files -n percona-orchestrator-cli
/usr/bin/orchestrator

%files -n percona-orchestrator-client
/usr/bin/orchestrator-client


%changelog
* Thu Jul 14 2022 Vadim Yalovets <vadim.yalovets@percona.com>
- DISTMYSQL-198 Create orchestrator-client packages for rpm based distributions.

* Tue May 03 2022 Vadim Yalovets <vadim.yalovets@percona.com>
- DISTMYSQL-156 Add conflict with openark orchestrator package.

* Tue Apr 07 2020 Evgeniy Patlan <evgeniy.patlan@percona.com>
- Initial build.
