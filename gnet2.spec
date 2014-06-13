# MD TODO !!!! rename src directory to just gnet !!!!
%define api	2.0
%define major	0
%define libname %mklibname %{name} %{api} %{major}
%define devname %mklibname %{name} -d

Summary:	A network library
Name:		gnet
Version:	2.0.8
Release:	16
Group:		System/Libraries
License:	LGPL
Url:		http://www.gnetlibrary.org
Source0:	gnet-%{version}.tar.bz2
Patch0:		gnet-2.0.8-examples.patch
Patch1:		gnet-2.0.8-automake113.patch
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
Obsoletes:	%{_lib}gnet-2.0_0 < 2.0.8-11

%description -n	%{libname}
Gnet is a simple network library.  It is writen in C, object-oriented,
and built upon glib.  It is intended to be small, fast, easy-to-use,
and easy to port.  The interface is similar to the interface for
Java's network library.

%package -n	%{devname}
Summary:	Header files for the Gnet library
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}
Obsoletes:	%{_lib}gnet-2.0-devel < 2.0.8-11

%description -n	%{devname}
This package allows you to develop applications that use the Gnet
library.

%prep
%setup -q
%apply_patches
chmod 755 doc/html

autoreconf -fi

%build
export CFLAGS="%{optflags} -fPIC"
%configure2_5x \
	--disable-static

%make

%install
%makeinstall_std

#remove unpackaged files
rm -rf %{buildroot}%{_datadir}/doc/libgnet%{api}-dev

%files -n %{libname}
%{_libdir}/libgnet-%{api}.so.%{major}*

%files -n %{devname}
%doc README COPYING ChangeLog NEWS TODO AUTHORS INSTALL HACKING doc/html
%doc %{_datadir}/gtk-doc/
%{_includedir}/gnet-%{api}
%{_datadir}/aclocal/*
%{_libdir}/gnet-%{api}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

