Summary:	A tool which displays the status of serial port modem lines
Name:		statserial
Version:	1.1
Release:	%mkrel 20
License:	BSD
Group:		Communications
URL:		ftp://sunsite.unc.edu/pub/Linux/system/serial/
Source:		ftp://sunsite.unc.edu/pub/Linux/system/serial/%{name}-%{version}.tar.bz2
Patch:		%{name}-1.1-config.patch
Patch1: 	%{name}-1.1-dev.patch
BuildRequires:	ncurses-devel
BuildRequires:	glibc-static-devel 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root

%description
The statserial utility displays a table of the signals on a standard 9-pin or
25-pin serial port and indicates the status of the handshaking lines.
Statserial is useful for debugging serial port and/or modem problems.

Install the statserial package if you need a tool to help debug serial port or
modem problems.

%prep

%setup -q
%patch -p1 -b .config
%patch1 -p1 -b .dev

%build
%make CFLAGS="%{optflags} -O3"

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/{%{_bindir},%{_mandir}/man1}

install -m 755 -s statserial %{buildroot}%{_bindir}/statserial
install -m 444 statserial.1 %{buildroot}%{_mandir}/man1/statserial.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING ChangeLog README
%{_bindir}/statserial
%{_mandir}/man1/statserial.1*


