%define name liblrdf
%define version 0.4.0

%define major 	2
%define real_name lrdf 
%define libname %mklibname %real_name %major

Name: 		%{name}
Summary: 	Library for handling RDF descriptions of audio plugins
Version: 	%{version}
Release: 	%mkrel 9

Source:		http://prdownloads.sourceforge.net/lrdf/%{name}-%{version}.tar.bz2
URL:		http://sourceforge.net/projects/lrdf
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	raptor-devel ladspa-devel

%description
liblrdf is a library for handling RDF (http://www.w3.org/RDF/)
descriptions of LADSPA (and potentially other format) plugins.

It allows grouping of plugins into trees for user slection and finer
description of plugins and ports than the .so format allows (for example
to indicatate textual equivalents of integer port values). It also
provides named and described defaults and presets, metadata and general
semnatic goodness. 

%package -n %{libname}
Summary: Main library for %name
Group: System/Libraries
Provides: %{name} = %{version}-%{release}

%description -n %{libname}
liblrdf is a library for handling RDF (http://www.w3.org/RDF/)
descriptions of LADSPA (and potentially other format) plugins.

It allows grouping of plugins into trees for user slection and finer
description of plugins and ports than the .so format allows (for example
to indicatate textual equivalents of integer port values). It also
provides named and described defaults and presets, metadata and general
semnatic goodness. 

%package -n %{libname}-common
Summary: File used by %name
Group: System/Libraries
Provides: %{name} = %{version}-%{release}

%description -n %{libname}-common
This packages contains various files required by %name.


%package -n %{libname}-devel
Summary: Headers for developing programs that will use %name
Group: Development/C++
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Provides: lib%{real_name}-devel = %{version}-%{release}

%description -n %{libname}-devel
This package contains the headers that programmers will need to develop
applications which will use libraries from %name.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
# (misc) remove this once the libcurl package is fixed and do not
# contain reference to /home, no rpmlint warning.
#perl -pi -e 's#-L/export/home/\w+##' $RPM_BUILD_ROOT/%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{libname}-common
%defattr(-,root,root)
%{_datadir}/ladspa/rdf/

%files -n %{libname}-devel
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_libdir}/pkgconfig/*.pc

