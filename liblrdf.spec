%define name liblrdf
%define version 0.4.0

%define major 	2
%define real_name lrdf 
%define libname %mklibname %real_name %major

Name: 		%{name}
Summary: 	Library for handling RDF descriptions of audio plugins
Version: 	%{version}
Release: 	13

Source:		http://prdownloads.sourceforge.net/lrdf/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/lrdf
License:	GPL
Group:		System/Libraries
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	raptor2-devel ladspa-devel

Patch0:		liblrdf-0.4.0-dontbuild-tests.patch
Patch1:		liblrdf-0.4.0-raptor2.patch	
Patch2:		liblrdf-0.4.0-raptor2-pkgconfig.patch
Patch3:		liblrdf-0.4.0-rename_clashing_md5_symbols.patch


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

%patch0
%patch1
%patch2
%patch3

libtoolize --copy --force --install --automake
aclocal
autoconf
autoheader
automake --add-missing --copy


%build
%configure2_5x --enable-static=no
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std
# (misc) remove this once the libcurl package is fixed and do not
# contain reference to /home, no rpmlint warning.
#perl -pi -e 's#-L/export/home/\w+##' %{buildroot}/%{_libdir}/*.la

#%if "%{_lib}" == "lib64"
#perl -pi -e "s|-L/usr/lib\b|-L%{_libdir}|g" %{buildroot}%{_libdir}/*.la
#%endif
rm -f %{buildroot}%{_libdir}/*.la

%clean
rm -rf %{buildroot}

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
%{_libdir}/pkgconfig/*.pc

