%global     commit 48754f28fe1050df58f2d9f7cd2becc019e2f486
%global     commit_short %(c=%{commit}; echo ${c:0:7})

Name:		qlipper
Version:	5.0.0
Release:	1.%{commit_short}%{?dist}
License:	GPLv3+
Summary:	Lightweight clipboard history
URL:		https://github.com/pvanek/qlipper
Source0:	https://github.com/pvanek/qlipper/archive/%{commit}.tar.gz#/%{name}-%{version}-%{commit_short}.tar.gz
BuildRequires:	cmake
BuildRequires:  desktop-file-utils
BuildRequires:  ImageMagick
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Help)


%description
Lightweight clipboard history applet.


%prep
%setup -n %{name}-%{commit}

%build
%cmake .
make %{?_smp_mflags}


%install
%{makeinstall} DESTDIR=%{buildroot}
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

install -d -D -m 755 %{buildroot}%{_datadir}/pixmaps
install -d -D -m 755 %{buildroot}%{_iconsdir}

install -D src/icons/%{name}.png %{buildroot}%{_iconsdir}
convert %{buildroot}%{_iconsdir}/%{name}.png %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

%files
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/%{name}/translations/*.qm
%{_datadir}/icons/hicolor/*/*/%{name}.png



%changelog
* Sun Oct 16 2016 Vaughan <devel at agrez dot net> - 5.0.0-1.48754f2
- Update to git commit: 48754f28fe1050df58f2d9f7cd2becc019e2f486

* Sat Sep 10 2016 Vaughan <devel at agrez dot net> - 5.0.0-0.dae06f3
- Drop patch0
- New version
- Update to git commit: dae06f31025aace991c72f37295f05236b16ab3d
- Build against Qt5

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 TI_Eugene <ti.eugene@gmail.com> - 2.0.2-1
- Version bump.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.1-6
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Apr 12 2013 TI_Eugene <ti.eugene@gmail.com> 2.0.1-2
- License upgraded to GPLv3+
- INSTALL_PREFIX removed from %%cmake flags
- "cross-platform" removed from %%description

* Sat Apr 06 2013 TI_Eugene <ti.eugene@gmail.com> 2.0.1-1
- initial packaging for Fedora
