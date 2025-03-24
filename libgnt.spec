Summary:	The GLib Ncurses Toolkit
Summary(pl.UTF-8):	Biblioteka GLib Ncurses Toolkit
Name:		libgnt
Version:	2.14.3
Release:	3
License:	GPL v2+
Group:		Libraries
Source0:	https://downloads.sourceforge.net/pidgin/%{name}-%{version}.tar.xz
# Source0-md5:	15c5e934fc5dec533a6d974639b54291
Patch0:		python3.patch
URL:		https://keep.imfreedom.org/libgnt/libgnt
BuildRequires:	glib2-devel >= 1:2.16.0
BuildRequires:	gtk-doc
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	meson >= 0.44.0
BuildRequires:	ncurses-devel
BuildRequires:	ncurses-ext-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python3-devel
BuildRequires:	rpm-build >= 4.6
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

%description -l pl.UTF-8
GNT to biblioteka narzędziowa ncurses do tworzenia graficznych
interfejsów użytkownika w trybie tekstowym w szybki i łatwy sposób.
Jeset oparta na bibliotekach GLib i ncurses.

Biblioteka powstała z konsolowego interfejsu użytkownika Finch,
stworzonego dla projektu libpurple, ale została wydzielona do
samodzielnego repozytorium.

%package devel
Summary:	Header files for GNT library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki GNT
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for GNT library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki GNT.

%package static
Summary:	Static GNT library
Summary(pl.UTF-8):	Statyczna biblioteka GNT
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static GNT library.

%description static -l pl.UTF-8
Statyczna biblioteka GNT.

%package apidocs
Summary:	GNT API documentation
Summary(pl.UTF-8):	Dokumentacja API biblioteki GNT
Group:		Documentation
Requires:	gtk-doc-common
BuildArch:	noarch

%description apidocs
GNT API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki GNT.

%prep
%setup -q
%patch -P 0 -p1

%{__sed} -i -e 's/ = library(/ = shared_library(/' wms/meson.build

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

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
