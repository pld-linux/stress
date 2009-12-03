Summary:	A tool which imposes a configurable amount of load on your system
Summary(pl.UTF-8):	Narzędzie powodujące konfigurowalne obciążenie systemu
Name:		stress
Version:	1.0.2
Release:	1
License:	GPL
Group:		Applications
Source0:	http://weather.ou.edu/~apw/projects/stress/%{name}-%{version}.tar.gz
# Source0-md5:	ad53eb802150bda8f898be9ebf3b4b36
Patch0:		%{name}-info.patch
URL:		http://weather.ou.edu/~apw/projects/stress/
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Stress is a tool which imposes a configurable amount of CPU, memory,
I/O, or disk stress on a POSIX-compliant operating system. It is
written in highly-portable ANSI C, and uses the GNU Autotools to
compile on a great number of UNIX-like operating systems.

Stress is not a benchmark. It is a tool used by system administrators
to evaluate how well their systems will scale, by kernel programmers
to evaluate perceived performance characteristics, and by systems
programmers to expose the classes of bugs which only or more
frequently manifest themselves when the system is under heavy load.

%description -l pl.UTF-8
Stress to narzędzie powodujące konfigurowane obciążenie procesora,
pamięci, wejścia/wyjścia lub dysku w systemie operacyjnym
kompatybilnym z POSIX. Jest napisane w dobrze przenośnym ANSI C i
używa do kompilacji GNU autotools, aby skompilować się na dużej
liczbie uniksowych systemów operacyjnych.

Stress to nie jest benchmark. To jest narzędzie używane przez
administratorów systemów do określania, jak ich systemy będą się
skalować; przez programistów jądra do określania odczuwalnej
charakterystyki wydajności; przez programistów systemowych do
ujawniania klas błędów, które objawiają się tylko (lub częściej się
objawiają) przy bardzo obciążonym systemie.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make} \
	AM_CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/stress.1*
%{_infodir}/*info*
