Summary:	A tool which imposes a configurable amount of load on your system
Summary(pl):	Narz�dzie powoduj�ce konfigurowalne obci��enie systemu
Name:		stress
Version:	0.18.8
Release:	1
License:	GPL
Group:		Applications
Source0:	http://weather.ou.edu/~apw/projects/stress/%{name}-%{version}.tar.gz
# Source0-md5:	160d41166d98a1e88c3f95f556633b71
Patch0:		%{name}-info.patch
Patch1:		%{name}-fix_build.patch
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

%description -l pl
Stress to narz�dzie powoduj�ce konfigurowane obci��enie procesora,
pami�ci, wej�cia/wyj�cia lub dysku w systemie operacyjnym
kompatybilnym z POSIX. Jest napisane w dobrze przeno�nym ANSI C i
u�ywa do kompilacji GNU autotools, aby skompilowa� si� na du�ej
liczbie uniksowych system�w operacyjnych.

Stress to nie jest benchmark. To jest narz�dzie u�ywane przez
administrator�w system�w do okre�lania, jak ich systemy b�d� si�
skalowa�; przez programist�w j�dra do okre�lania odczuwalnej
charakterystyki wydajno�ci; przez programist�w systemowych do
ujawniania klas b��d�w, kt�re objawiaj� si� tylko (lub cz�ciej si�
objawiaj�) przy bardzo obci��onym systemie.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

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

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/stress.1*
%{_infodir}/*info*
