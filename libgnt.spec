%define		commit	6b9bc53302ef

Summary:	The GLib Ncurses Toolkit
Name:		libgnt
Version:	2.14.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	https://bitbucket.org/pidgin/libgnt/get/v%{version}.tar.bz2
# Source0-md5:	f0be976b9e89e8990f5083100fa0513c
URL:		https://bitbucket.org/pidgin/libgnt/
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk-doc
BuildRequires:	libxml2-devel >= 2.6.0
BuildRequires:	meson >= 0.37.0
BuildRequires:	ncurses-devel
BuildRequires:	ncurses-ext-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.727
Requires:	glib2 >= 1:2.16.0
Requires:	libxml2 >= 2.6.0
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
%setup -q -n pidgin-libgnt-%{commit}

%build
%meson build
%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

rm $RPM_BUILD_ROOT%{_libdir}/gnt/*.a

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README.md
%attr(755,root,root) %{_libdir}/libgnt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnt.so.0
%dir %{_libdir}/gnt
%attr(755,root,root) %{_libdir}/gnt/irssi.so
%attr(755,root,root) %{_libdir}/gnt/s.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnt.so
%dir %{_includedir}/gnt
%{_includedir}/gnt/*.h
%{_pkgconfigdir}/gnt.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnt.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libgnt
