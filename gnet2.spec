%define api_version 2.0
%define major 0
%define libname %mklibname gnet-%{api_version}_ %{major}
%define develname %mklibname gnet-%{api_version} -d

Summary:	A network library
Name:		gnet2
Version:	2.0.8
Release:	10
Group:		System/Libraries
License:	LGPL
URL:		http://www.gnetlibrary.org
Source0:	gnet-%{version}.tar.bz2
Patch0:		gnet-2.0.8-examples.patch
BuildRequires:	pkgconfig(glib-2.0)

%description
Gnet is a simple network library.  It is writen in C, object-oriented,
and built upon glib.  It is intended to be small, fast, easy-to-use,
and easy to port.  The interface is similar to the interface for
Java's network library.

Features:
  * TCP 'client' sockets
  * TCP 'server' sockets
  * Non-blocking TCP sockets
  * UDP
  * IP Multicast
  * Internet address abstraction

%package -n	%{libname}
Summary:	Libgnet, a network library
Group:		System/Libraries
Provides:	lib%{name} = %{version}-%{release}

%description -n	%{libname}
Gnet is a simple network library.  It is writen in C, object-oriented,
and built upon glib.  It is intended to be small, fast, easy-to-use,
and easy to port.  The interface is similar to the interface for
Java's network library.

%package -n	%{develname}
Summary:	Header files for the Gnet library
Group:		Development/C
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	libgnet-%{api_version}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n	%{develname}
Gnet is a simple network library.  It is writen in C, object-oriented,
and built upon glib.
This package allows you to develop applications that use the Gnet
library.

%prep
%setup -q -n gnet-%{version}
%patch0 -p1
chmod 755 doc/html

%build
autoreconf -fi
export CFLAGS="%{optflags} -fPIC"
%configure2_5x --disable-static

%make

%install
%makeinstall_std

#remove unpackaged files
rm -rf %{buildroot}%{_datadir}/doc/libgnet%{api_version}-dev
rm -fr %{buildroot}%{_datadir}/gtk-doc/

%files -n %{libname}
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%doc README COPYING ChangeLog NEWS TODO AUTHORS INSTALL HACKING doc/html
%{_includedir}/gnet-2.0
%{_datadir}/aclocal/*
%{_libdir}/gnet-2.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.8-7mdv2011.0
+ Revision: 664857
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.8-6mdv2011.0
+ Revision: 605468
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.8-5mdv2010.1
+ Revision: 521130
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 2.0.8-4mdv2010.0
+ Revision: 424994
- rebuild

* Mon Jul 14 2008 Oden Eriksson <oeriksson@mandriva.com> 2.0.8-3mdv2009.0
+ Revision: 234792
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.0.8-2mdv2009.0
+ Revision: 221080
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Feb 04 2008 Götz Waschk <waschk@mandriva.org> 2.0.8-1mdv2008.1
+ Revision: 162043
- new version

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 2.0.7-4mdv2008.1
+ Revision: 150112
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Jul 21 2007 Adam Williamson <awilliamson@mandriva.org> 2.0.7-3mdv2008.0
+ Revision: 54155
- rebuild for 2008
- new devel policy


* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 18:20:25 (53607)
- rebuild

* Sun Aug 06 2006 Olivier Thauvin <nanardon@mandriva.org>
+ 08/06/06 18:18:24 (53606)
Import gnet2

* Tue Jul 26 2005 Olivier Thauvin <nanardon@mandriva.org> 2.0.7-1mdk
- 2.0.7

* Thu Jun 10 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 2.0.5-3mdk
- really fix buildrequires

* Tue Jun 08 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.0.5-2mdk
- fix buildrequires

* Mon May 31 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 2.0.5-1mdk 
- 2.0.5
- misc spec file fixes

