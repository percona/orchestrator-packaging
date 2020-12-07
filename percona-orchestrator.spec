%define debug_package %{nil}

Name:           percona-orchestrator
Version:        %{version}
Release:        1%{?dist}
Summary:        MySQL replication topology management and HA

Group:          Applications/Databases
License:        Apache 2.0
URL:            https://github.com/github/orchestrator
Source0:        %{name}-%{version}.tar.gz
Epoch:          2

BuildRequires:  gcc make perl-Digest-SHA
Requires:       jq >= 1.5
Requires:       oniguruma

%description
MySQL replication topology management and HA
 
%prep
%setup -q -n %{name}-%{version}


%build
ls
bash script/build


%install
%{__rm} -rf %{buildroot}
%{__install} -D -m 0644 etc/systemd/orchestrator.service %{buildroot}/lib/systemd/system/orchestrator.service
%{__install} -D -d -m 0755 %{buildroot}/usr/local/orchestrator/
%{__cp} -r bin/resources %{buildroot}/usr/local/orchestrator/resources
%{__cp}  bin/orchestrator %{buildroot}/usr/local/orchestrator/
%{__cp}  conf/orchestrator-sample* %{buildroot}/usr/local/orchestrator/

%files
%doc LICENSE
%config /lib/systemd/system/orchestrator.service
/usr/local/orchestrator/resources
%attr(755, root, root) /usr/local/orchestrator/orchestrator
/usr/local/orchestrator/orchestrator-sample.conf.json
/usr/local/orchestrator/orchestrator-sample-sqlite.conf.json


%changelog
* Tue Apr 07 2020 Evgeniy Patlan <evgeniy.patlan@percona.com>
- Initial build.
