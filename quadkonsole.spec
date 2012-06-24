Summary:	KDE application that embeds Konsole kparts in a grid layout
Summary(pl):	Aplikacja KDE osadzaj�ca konsol� KDE w uk�adzie siatki
Name:		quadkonsole
Version:	2.0.1
Release:	0.4
License:	GPL v2
Group:		X11/Applications
Source0:	http://nomis80.org/quadkonsole/%{name}-%{version}.tar.gz
# Source0-md5:	a983a46d98be6cb5de66b80de04f97f7
URL:		http://kde-apps.org/content/show.php?content=22482
BuildRequires:	automake
BuildRequires:	kdelibs-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	kdelibs >= 3.3.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
QuadKonsole shows multiple konsoles in one window, so it can be
minimized/maximized at once. Other advantages are less memory
consumption, faster startup, auto align of konsoles and easy
navigation.

The number of rows and columns of Konsoles is 2 by 2 by default, but
can be specified on the command-line. The settings of the Konsoles can
be accessed using the right mouse button and can be saved. These
settings apply to the system globally, to all Konsole kparts. Konsole
widgets get focus as soon as the mouse hovers on them (focus follows
mouse). This can be disabled on the command-line. Use CTRL + SHIFT +
arrow key to move from konsole to konsole.

%description -l pl
QuadKonsole wy�wietla wiele konsol w jednym oknie, dzi�ki temu mo�e
zosta� zminimalizowana/zmaksymalizowana za jednym razem. Inne korzy�ci
to mi�dzy innymi mniejszy pob�r pami�ci, szybszy start, automatyczne
wyr�wnywanie konsol oraz �atwa nawigacja.

Domy�lna ilo�� kolumn i wierszy dla konsol to 2 na 2, ale warto�ci te
mog� by� ustawione w linii polece�. Ustawienia konsol s� dost�pne pod
prawym przyciskiem myszki a zapisane ustawienia s� globalne i odnosz�
si� do wszystkich osadzanych element�w. Konsole aktywuje si� poprzez
kursor myszki (co mo�e zosta� wy��czone w linii polece�) oraz poprzez
kursory klawiatury z wci�ni�tymi CTRL i SHIFT.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.* admin
%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
mv $RPM_BUILD_ROOT/usr/share/applnk/Utilities/*.desktop $RPM_BUILD_ROOT%{_desktopdir}/kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/quadkonsole
%{_desktopdir}/kde/quadkonsole.desktop
