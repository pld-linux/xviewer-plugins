Summary:	A collection of plugins for Xviewer
Summary(pl.UTF-8):	Zestaw wtyczek do przeglądarki obrazków Xviewer
Name:		xviewer-plugins
Version:	3.4.1
Release:	1
License:	GPL v2+
Group:		X11/Applications
#Source0Download: https://github.com/linuxmint/xviewer-plugins/tags
Source0:	https://github.com/linuxmint/xviewer-plugins/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	02dfa3413f5511f6cadc7b9aa373a597
URL:		https://github.com/linuxmint/xviewer-plugins
BuildRequires:	clutter-devel >= 1.9.4
BuildRequires:	clutter-gtk-devel >= 1.1.2
BuildRequires:	gettext-tools >= 0.19.7
BuildRequires:	glib2-devel >= 1:2.32.0
BuildRequires:	gtk+3-devel >= 3.3.8
BuildRequires:	libchamplain-devel >= 0.12
BuildRequires:	libexif-devel >= 1:0.6.16
BuildRequires:	libpeas-devel >= 0.7.4
BuildRequires:	libpeas-gtk-devel >= 1.12.0
BuildRequires:	meson >= 0.58.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	python3-devel >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	xviewer-devel >= 3.2.1
Requires(post,postun):	glib2 >= 1:2.32.0
Requires:	clutter >= 1.9.4
Requires:	clutter-gtk >= 1.1.2
Requires:	glib2 >= 1:2.32.0
Requires:	gtk+3 >= 3.3.8
Requires:	libchamplain >= 0.12
Requires:	libexif >= 1:0.6.16
Requires:	libpeas >= 0.7.4
Requires:	libpeas-gtk >= 1.12.0
Requires:	xviewer >= 3.2.1
Suggests:	libpeas-loader-python >= 0.7.4
Suggests:	python-pygobject3 >= 3.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides collection of plugins for use with Xviewer.

%description -l pl.UTF-8
Ten pakiet dostarcza zestaw wtyczek do przeglądarki obrazków Xviewer.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc debian/changelog

%{_libdir}/xviewer/plugins/exif-display.plugin
%attr(755,root,root) %{_libdir}/xviewer/plugins/libexif-display.so
%{_datadir}/glib-2.0/schemas/org.x.viewer.plugins.exif-display.gschema.xml
%{_datadir}/metainfo/xviewer-exif-display.metainfo.xml

%{_libdir}/xviewer/plugins/export-to-folder.plugin
%{_libdir}/xviewer/plugins/export-to-folder.py
%{_datadir}/xviewer/plugins/export-to-folder
%{_datadir}/glib-2.0/schemas/org.x.viewer.plugins.export-to-folder.gschema.xml
%{_datadir}/metainfo/xviewer-export-to-folder.metainfo.xml

%{_libdir}/xviewer/plugins/map.plugin
%attr(755,root,root) %{_libdir}/xviewer/plugins/libmap.so
%{_datadir}/metainfo/xviewer-map.metainfo.xml

%{_libdir}/xviewer/plugins/pythonconsole.plugin
%{_libdir}/xviewer/plugins/pythonconsole
%{_datadir}/xviewer/plugins/pythonconsole
%{_datadir}/glib-2.0/schemas/org.x.viewer.plugins.pythonconsole.gschema.xml
%{_datadir}/metainfo/xviewer-pythonconsole.metainfo.xml

%{_libdir}/xviewer/plugins/send-by-mail.plugin
%attr(755,root,root) %{_libdir}/xviewer/plugins/libsend-by-mail.so
%{_datadir}/metainfo/xviewer-send-by-mail.metainfo.xml

%{_libdir}/xviewer/plugins/slideshowshuffle.plugin
%{_libdir}/xviewer/plugins/slideshowshuffle.py
%{_datadir}/metainfo/xviewer-slideshowshuffle.metainfo.xml
