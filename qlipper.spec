Name:		qlipper
Version:	2.0.1
Release:	2%{?dist}
License:	GPLv3+
Summary:	Lightweight clipboard history
URL:		http://code.google.com/p/qlipper
Source0:	http://qlipper.googlecode.com/files/%{name}-%{version}.tar.bz2
Source1:	FindQxt.cmake
Source2:	FindQtSingleApplication.cmake
Patch0:		%{name}-%{version}-qxt_qtsa.patch
BuildRequires:	cmake, desktop-file-utils
BuildRequires:	pkgconfig(QtGui), libqxt-devel, qtsingleapplication-devel

%description
Lightweight clipboard history applet.

%prep
%setup -q
mkdir cmake
cp %{SOURCE1} cmake
cp %{SOURCE2} cmake
%patch0 -p 0
# be assured
%{__rm} -rf qxt qtsingleapplication

%build
mkdir build
pushd build
%cmake -DCMAKE_BUILD_TYPE=release  -DUSE_SYSTEM_QXT=ON -DUSE_SYSTEM_QTSINGLEAPPLICATION=ON ..
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
* Fri Apr 12 2013 TI_Eugene <ti.eugene@gmail.com> 2.0.1-2
- License upgraded to GPLv3+
- INSTALL_PREFIX removed from %%cmake flags
- "cross-platform" removed from %%description

* Sat Apr 06 2013 TI_Eugene <ti.eugene@gmail.com> 2.0.1-1
- initial packaging for Fedora
