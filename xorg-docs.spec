Summary:	X.org documentation
Summary(pl.UTF-8):	Dokumentacja X.org
Name:		xorg-docs
Version:	1.5
Release:	2
License:	MIT
Group:		Documentation
Source0:	http://xorg.freedesktop.org/releases/individual/doc/%{name}-%{version}.tar.bz2
# Source0-md5:	359ac83ad27eecd5588914ba8715301d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
# not really used yet
#BuildRequires:	docbook-utils
#BuildRequires:	xorg-sgml-doctools >= 1.1.1
BuildRequires:	xorg-util-util-macros >= 1.1.2
Obsoletes:	xorg-docs-ps
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_target_platform	%{_target}

%description
X.org documentation.

%description -l pl.UTF-8
Dokumentacja X.org.

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
