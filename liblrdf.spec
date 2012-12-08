%define major 2
%define real_name lrdf
%define libname %mklibname %{real_name} %{major}

Name:		liblrdf
Summary:	Library for handling RDF descriptions of audio plugins
Version:	0.4.0
Release:	14

Source:		http://prdownloads.sourceforge.net/lrdf/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/lrdf
License:	GPL
Group:		System/Libraries
BuildRequires:	raptor2-devel
BuildRequires:	ladspa-devel

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
Summary:	Main library for %{name}
Group:		System/Libraries

%description -n %{libname}
liblrdf is a library for handling RDF (http://www.w3.org/RDF/)
descriptions of LADSPA (and potentially other format) plugins.

It allows grouping of plugins into trees for user slection and finer
description of plugins and ports than the .so format allows (for example
to indicatate textual equivalents of integer port values). It also
provides named and described defaults and presets, metadata and general
semnatic goodness.

%package -n %{libname}-common
Summary:	File used by %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}-common
This packages contains various files required by %{name}.

%package -n %{libname}-devel
Summary:	Headers for developing programs that will use %{name}
Group:		Development/C++
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{real_name}-devel = %{version}-%{release}

%description -n %{libname}-devel
This package contains the headers that programmers will need to develop
applications which will use libraries from %{name}.

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
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/*.so.*

%files -n %{libname}-common
%{_datadir}/ladspa/rdf/

%files -n %{libname}-devel
%doc AUTHORS COPYING ChangeLog NEWS README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc



%changelog
* Sun Dec 11 2011 Frank Kober <emuse@mandriva.org> 0.4.0-13
+ Revision: 740228
- rebuild removing libtool archive and static lib from devel package

* Wed Sep 21 2011 Alexander Barakin <abarakin@mandriva.org> 0.4.0-12
+ Revision: 700759
- added autoconf to prep section
- raptor2 fix
- imported package liblrdf

* Mon Jun 20 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-11
+ Revision: 686315
- avoid pulling 32 bit libraries on 64 bit arch

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-10
+ Revision: 661490
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-9mdv2011.0
+ Revision: 602571
- rebuild

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-8mdv2010.1
+ Revision: 520881
- rebuilt for 2010.1

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.4.0-7mdv2010.0
+ Revision: 425593
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.4.0-6mdv2009.0
+ Revision: 222923
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-5mdv2008.1
+ Revision: 178964
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Tue Jan 16 2007 Nicolas Lécureuil <neoclust@mandriva.org>
+ 2007-01-16 13:43:36 (109479)
- Rebuild against new curl
- Import liblrdf

* Mon Nov 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.4.0-2mdk
- rebuilt against openssl-0.9.8a

* Thu Aug 25 2005 Austin Acton <austin@mandriva.org> 0.4.0-1mdk
- 0.4.0
- new URL's

* Tue Jul 20 2004 Austin Acton <austin@mandrake.org> 0.3.7-1mdk
- 0.3.7

* Sat Jul 03 2004 Michael Scherer <misc@mandrake.org> 0.3.5-2mdk 
- rebuild for new libcurl
- remove libtool hack

* Mon Feb 16 2004 Austin Acton <austin@mandrake.org> 0.3.5-1mdk
- 0.3.5
- major 2

