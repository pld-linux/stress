Summary:	A tool which imposes a configurable amount of load on your system.
Name:		stress
Version:	0.18.1
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://weather.ou.edu/~apw/projects/stress/%{name}-%{version}.tar.gz
# Source0-md5:	6d17ea5e752653021f3f96077541ade7
URL:		http://weather.ou.edu/~apw/projects/stress/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
stress is a tool which imposes a configurable amount of CPU, memory,
I/O, or disk stress on a POSIX-compliant operating system. It is
written in highly-portable ANSI C, and uses the GNU Autotools to
compile on a great number of UNIX-like operating systems.

stress is not a benchmark. It is a tool used by system administrators
to evaluate how well their systems will scale, by kernel programmers
to evaluate perceived performance characteristics, and by systems
programmers to expose the classes of bugs which only or more
frequently manifest themselves when the system is under heavy load.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/stress.1*
%{_infodir}/*info*
