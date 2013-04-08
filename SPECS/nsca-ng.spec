Summary: NSCA alternative
Name: nsca-ng 
Version: 1.0
Release: 1%{?dist}
License: GPLv2
URL: http://www.nsca-ng.org/
Group: System Environment/Daemons
Source: http://www.nsca-ng.org/download/nsca-ng-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires:   make
BuildRequires: make

%description
The NSCA-ng package provides a client-server pair which makes the "Nagios
command file" accessible to remote systems. This allows for submitting passive
check results, downtimes, and many other commands to Nagios (or compatible
monitoring solutions).

%prep
%setup -q

%build
./build-aux/make-openssl
./build-aux/make-confuse
%configure --disable-server
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall \
	MANDIR="%{buildroot}%{_mandir}/man1/"

%files
%config %{_sysconfdir}/send_nsca.cfg
%attr(0755, root, root) %{_sbindir}/send_nsca
%doc %{_mandir}/man?/*
