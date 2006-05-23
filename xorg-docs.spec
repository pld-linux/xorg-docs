Summary:	X.org documentation
Summary(pl):	Dokumentacja X.org
Name:		xorg-docs
Version:	1.2
Release:	1
License:	MIT
Group:		Documentation
Source0:	http://xorg.freedesktop.org/releases/individual/doc/xorg-docs-%{version}.tar.bz2
# Source0-md5:	f817c5df43817846c1b27bac83da74d7
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org documentation.

%description -l pl
Dokumentacja X.org.

%package ps
Summary:	X.org documentation in PostScript format
Summary(pl):	Dokumentacja X.org w formacie PostScript
Group:		Documentation

%description ps
X.org documentation in PostScript format.

%description ps -l pl
Dokumentacja X.org w formacie PostScript.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{_mandir}/man7/*.7*

%files ps
%defattr(644,root,root,755)
%doc ChangeLog README $RPM_BUILD_ROOT%{_datadir}/X11/doc/hardcopy/*
