%global astal_commit 69efb4c91e590adcb5a3d8938454f987982e3891
%global astal_shortcommit %(c=%{astal_commit}; echo ${c:0:7})
%global bumpver 1

%global _lto_cflags %{nil}

%define libname %mklibname astal-libs
%define devname %mklibname astal-libs -d

Name:           astal-libs
Version:        1~%{bumpver}.git%{astal_shortcommit}
Release:        1
Summary:        Astal libraries
Group:          System/Libraries
License:        LGPL-2.1-only
URL:            https://github.com/Aylur/astal
Source0:        %{url}/archive/%{astal_commit}/%{name}-%{astal_shortcommit}.tar.gz

BuildRequires:  gcc
BuildRequires:  meson
BuildRequires:  pkgconfig(appmenu-glib-translator)
BuildRequires:  pkgconfig(astal-3.0)
BuildRequires:  pkgconfig(astal-4-4.0)
BuildRequires:  pkgconfig(astal-io-0.1)
BuildRequires:  pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(pam)
BuildRequires:  python3
BuildRequires:  vala
BuildRequires:  valadoc
BuildRequires:	pkgconfig(libnma)
BuildRequires:	pkgconfig(cava)

Requires: cava

%description
%{summary}.

%package -n %{libname}
Summary:    %{summary}
Group:      System/Libraries
Provides:   %{libname} = %{EVRD}

%global __requires_exclude ^%{_libdir}
%description -n %{libname}
%{summary}.

%package -n %{devname}
Summary:  Development files for %{name}
Group:    Development/C
Requires: %{libname} = %{EVRD}


%description -n %{devname}
Development files (Headers etc.) for %{name}.

%prep
%autosetup -n astal-%{astal_commit} -p1

%build
cd lib
for lib in $(find -maxdepth 1 -mindepth 1 -type d -not -path ./astal); do
pushd $lib
%meson --auto-features=auto
%meson_build
popd
done

%install
cd lib
for lib in $(find -maxdepth 1 -mindepth 1 -type d -not -path ./astal); do
pushd $lib
%meson_install
popd
done
sed -i 's/ cava,//' %{buildroot}%{_libdir}/pkgconfig/astal-cava-0.1.pc
rm -rf %{buildroot}%{_includedir}/cava
rm -rf %{buildroot}%{_datadir}/consolefonts/cava.psf
rm -rf %{buildroot}%{_libdir}/pkgconfig/cava.pc

%files -n %{libname}
%license LICENSE
%config(noreplace) /etc/pam.d/astal-auth
%{_bindir}/astal-apps
%{_bindir}/astal-auth
%{_bindir}/astal-battery
%{_bindir}/astal-greet
%{_bindir}/astal-hyprland
%{_bindir}/astal-mpris
%{_bindir}/astal-notifd
%{_bindir}/astal-power-profiles
%{_bindir}/astal-river
%{_bindir}/astal-tray
%{_libdir}/girepository-1.0/AstalApps-0.1.typelib
%{_libdir}/girepository-1.0/AstalAuth-0.1.typelib
%{_libdir}/girepository-1.0/AstalBattery-0.1.typelib
%{_libdir}/girepository-1.0/AstalBluetooth-0.1.typelib
%{_libdir}/girepository-1.0/AstalCava-0.1.typelib
%{_libdir}/girepository-1.0/AstalGreet-0.1.typelib
%{_libdir}/girepository-1.0/AstalHyprland-0.1.typelib
%{_libdir}/girepository-1.0/AstalMpris-0.1.typelib
%{_libdir}/girepository-1.0/AstalNetwork-0.1.typelib
%{_libdir}/girepository-1.0/AstalNotifd-0.1.typelib
%{_libdir}/girepository-1.0/AstalPowerProfiles-0.1.typelib
%{_libdir}/girepository-1.0/AstalRiver-0.1.typelib
%{_libdir}/girepository-1.0/AstalTray-0.1.typelib
%{_libdir}/girepository-1.0/AstalWp-0.1.typelib
%{_libdir}/libastal-apps.so.0{,.*}
%{_libdir}/libastal-auth.so.0{,.*}
%{_libdir}/libastal-battery.so.0{,.*}
%{_libdir}/libastal-bluetooth.so.0{,.*}
%{_libdir}/libastal-cava.so.0{,.*}
%{_libdir}/libastal-greet.so.0{,.*}
%{_libdir}/libastal-hyprland.so.0{,.*}
%{_libdir}/libastal-mpris.so.0{,.*}
%{_libdir}/libastal-network.so.0{,.*}
%{_libdir}/libastal-notifd.so.0{,.*}
%{_libdir}/libastal-power-profiles.so.0{,.*}
%{_libdir}/libastal-river.so.0{,.*}
%{_libdir}/libastal-tray.so.0{,.*}
%{_libdir}/libastal-wireplumber.so.0{,.*}

%files -n %{devname}
%{_datadir}/gir-1.0/Astal*-0.1.gir
%{_datadir}/vala/vapi/astal-*-0.1.deps
%{_datadir}/vala/vapi/astal-*-0.1.vapi
%{_includedir}/astal-*.h
%{_includedir}/astal/
%{_libdir}/libastal-apps.so
%{_libdir}/libastal-auth.so
%{_libdir}/libastal-battery.so
%{_libdir}/libastal-bluetooth.so
%{_libdir}/libastal-cava.so
%{_libdir}/libastal-greet.so
%{_libdir}/libastal-hyprland.so
%{_libdir}/libastal-mpris.so
%{_libdir}/libastal-network.so
%{_libdir}/libastal-notifd.so
%{_libdir}/libastal-power-profiles.so
%{_libdir}/libastal-river.so
%{_libdir}/libastal-tray.so
%{_libdir}/libastal-wireplumber.so
%{_libdir}/pkgconfig/astal-*.pc

