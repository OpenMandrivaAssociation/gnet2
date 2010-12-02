%define name	gnet2
%define	version	2.0.8
%define	release	%mkrel 6

%define api_version 2.0
%define major 0
%define libname %mklibname gnet-%{api_version}_ %{major}
%define develname %mklibname gnet-%{api_version} -d

Summary:	A network library
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.gnetlibrary.org
License:	LGPL
Source0:	gnet-%{version}.tar.bz2
Group:		System/Libraries
BuildRequires:	glib2-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
Obsoletes:	%{mklibname gnet-%{api_version}_ 0 -d}

%description -n	%{develname}
Gnet is a simple network library.  It is writen in C, object-oriented,
and built upon glib.
This package allows you to develop applications that use the Gnet
library.

%prep

%setup -q -n gnet-%{version}
chmod 755 doc/html

%build
export CFLAGS="%{optflags} -fPIC"

%configure2_5x

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

#remove unpackaged files
rm -rf %{buildroot}%{_datadir}/doc/libgnet%{api_version}-dev
rm -fr %{buildroot}%{_datadir}/gtk-doc/

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-, root, root)
%doc README COPYING ChangeLog NEWS TODO AUTHORS INSTALL HACKING doc/html
%{_includedir}/gnet-2.0
%{_datadir}/aclocal/*
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/gnet-2.0
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


