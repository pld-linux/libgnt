Summary:	The GLib Ncurses Toolkit
Name:		libgnt
Version:	2.14.1
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/pidgin/%{name}-%{version}.tar.xz
# Source0-md5:	bd10a0c397e780f1432d72bdb2d8a61f
URL:		https://keep.imfreedom.org/libgnt/libgnt
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk-doc
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	meson >= 0.41.0
BuildRequires:	ncurses-devel
BuildRequires:	ncurses-ext-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	sed >= 4.0
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.16.0
Requires:	libxml2 >= 1:2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNT is an ncurses toolkit for creating text-mode graphical user
interfaces in a fast and easy way. It is based on GLib and ncurses.

It was born out of the console-based UI, Finch, for the libpurple
project, but has now been split into its own independent repository.

%package devel
Summary:	Header files for GNT library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for GNT library.

%package static
Summary:	Static GNT library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GNT library.

%package apidocs
Summary:	GNT API documentation
Group:		Documentation
Requires:	gtk-doc-common
%if "%{_rpmversion}" >= "4.6"
BuildArch:	noarch
%endif

%description apidocs
GNT API documentation.

%prep
%setup -q

%{__sed} -i -e 's/ = library(/ = shared_library(/' wms/meson.build

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog README.md
%attr(755,root,root) %{_libdir}/libgnt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnt.so.0
%dir %{_libdir}/gnt
%attr(755,root,root) %{_libdir}/gnt/irssi.so
%attr(755,root,root) %{_libdir}/gnt/s.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnt.so
%{_includedir}/gnt
%{_pkgconfigdir}/gnt.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnt.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgnt
