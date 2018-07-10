Summary:	A tool which displays the status of serial port modem lines
Name:		statserial
Version:	1.1
Release:	34
License:	BSD
Group:		Communications
URL:		ftp://sunsite.unc.edu/pub/Linux/system/serial/
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/serial/%{name}-%{version}.tar.bz2
Patch0:		%{name}-1.1-config.patch
Patch1: 	%{name}-1.1-dev.patch
Patch2:		statserial-1.1-LDFLAGS.diff
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
%patch0 -p1 -b .config
%patch1 -p1 -b .dev
%patch2 -p0 -b .LDFLAGS

%build
%make CFLAGS="%{optflags}" LDFLAGS="%{ldflags} -static"

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/{%{_bindir},%{_mandir}/man1}

install -m 755 statserial %{buildroot}%{_bindir}/statserial
install -m 444 statserial.1 %{buildroot}%{_mandir}/man1/statserial.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING ChangeLog README
%{_bindir}/statserial
%{_mandir}/man1/statserial.1*


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-25mdv2011.0
+ Revision: 670203
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-24mdv2011.0
+ Revision: 607753
- rebuild

* Mon Mar 15 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-23mdv2010.1
+ Revision: 520231
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.1-22mdv2010.0
+ Revision: 427216
- rebuild

* Mon Dec 22 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1-21mdv2009.1
+ Revision: 317286
- use %%ldflags

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.1-20mdv2009.0
+ Revision: 225494
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1-19mdv2008.1
+ Revision: 179540
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Fri Mar 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1-18mdv2007.1
+ Revision: 145159
- Import statserial

* Fri Mar 16 2007 Oden Eriksson <oeriksson@mandriva.com> 1.1-18mdv2007.1
- use the %%mkrel macro
- bunzip patches

* Wed Oct 27 2004 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.1-17mdk
- fix build

