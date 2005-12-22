Summary:	X.org documentation
Summary(pl):	Dokumentacja X.org
Name:		xorg-docs
Version:	1.0.1
Release:	0.1
License:	MIT
Group:		Documentation
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/doc/%{name}-X11R7.0-%{version}.tar.bz2
# Source0-md5:	ac0d76afa46ef5da9e1cf33558f4b303
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
%setup -q -n %{name}-X11R7.0-%{version}

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
