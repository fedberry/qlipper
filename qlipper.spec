Name:		qlipper
Version:	2.0.2
Release:	2%{?dist}
License:	GPLv3+
Summary:	Lightweight clipboard history
URL:		http://code.google.com/p/qlipper
Source0:	http://qlipper.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		%{name}-2.0.2-qxt_qtsa.patch
BuildRequires:	cmake, desktop-file-utils
BuildRequires:	pkgconfig(QtGui), libqxt-devel, qtsingleapplication-devel

%description
Lightweight clipboard history applet.


%prep
%setup -q
#mkdir cmake
#cp %{SOURCE1} cmake
#cp %{SOURCE2} cmake
%patch0 -p 0
# be assured
%{__rm} -rf qxt qtsingleapplication


%build
mkdir build
pushd build
%cmake -DCMAKE_BUILD_TYPE=release ..
make %{?_smp_mflags}
popd


%install
pushd build
%{makeinstall} DESTDIR=%{buildroot}
popd
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop


%files
%doc COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
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
