Summary:	X.org documentation
Summary(pl.UTF-8):	Dokumentacja X.org
Name:		xorg-docs
Version:	1.3
Release:	1
License:	MIT
Group:		Documentation
Source0:	http://xorg.freedesktop.org/releases/individual/doc/xorg-docs-%{version}.tar.bz2
# Source0-md5:	792d41a7a9f2e652b2ede4538c4bdf14
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
# not really used yet
#BuildRequires:	docbook-utils
#BuildRequires:	xorg-sgml-doctools >= 1.1.1
BuildRequires:	xorg-util-util-macros >= 1.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org documentation.

%description -l pl.UTF-8
Dokumentacja X.org.

%package ps
Summary:	X.org documentation in PostScript format
Summary(pl.UTF-8):	Dokumentacja X.org w formacie PostScript
Group:		Documentation

%description ps
X.org documentation in PostScript format.

%description ps -l pl.UTF-8
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
