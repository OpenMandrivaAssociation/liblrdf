%define major 2
%define libname %mklibname lrdf %{major}
%define devname %mklibname lrdf -d

Summary:	Library for handling RDF descriptions of audio plugins
Name:		liblrdf
Version:	0.4.0
Release:	25
License:	GPLv2
Group:		System/Libraries
Url:		http://sourceforge.net/projects/lrdf
Source0:	http://prdownloads.sourceforge.net/lrdf/%{name}-%{version}.tar.gz
Patch0:		liblrdf-0.4.0-dontbuild-tests.patch
Patch1:		liblrdf-0.4.0-raptor2.patch
Patch2:		liblrdf-0.4.0-raptor2-pkgconfig.patch
Patch3:		liblrdf-0.4.0-rename_clashing_md5_symbols.patch
Patch4:		liblrdf-automake-1.13.patch
BuildRequires:	ladspa-devel
BuildRequires:	pkgconfig(raptor2)

%description
liblrdf is a library for handling RDF (http://www.w3.org/RDF/)
descriptions of LADSPA (and potentially other format) plugins.

It allows grouping of plugins into trees for user slection and finer
description of plugins and ports than the .so format allows (for example
to indicatate textual equivalents of integer port values). It also
provides named and described defaults and presets, metadata and general
semnatic goodness.

%package common
Summary:	File used by %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{_lib}lrdf2-common < 0.4.0-16

%description common
This packages contains various files required by %{name}.

%package -n %{libname}
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
This package contains the shared library for %{name}.

%package -n %{devname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}lrdf2-devel < 0.4.0-16

%description -n %{devname}
This package contains the headers that programmers will need to develop
applications which will use libraries from %{name}.

%prep
%autosetup -p1
autoreconf -fi

%build
%configure --disable-static
%make_build

%install
%make_install

%files common
%{_datadir}/ladspa/rdf/

%files -n %{libname}
%{_libdir}/liblrdf.so.%{major}*

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog NEWS README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
