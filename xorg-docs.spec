Summary:	X.org documentation
Summary(pl.UTF-8):	Dokumentacja X.org
Name:		xorg-docs
Version:	1.7.1
Release:	2
License:	MIT
Group:		Documentation
Source0:	http://xorg.freedesktop.org/releases/individual/doc/%{name}-%{version}.tar.bz2
# Source0-md5:	ce5a04d87b330b9091576b3410dc26d3
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
Obsoletes:	xorg-docs-ps
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%configure \
%ifarch x32
	--host=%{_target_platform} \
	--build=%{_target_platform} \
%else
	--host=%{_host} \
	--build=%{_host} \
%endif
	--without-fop
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# package just HTML, omit txt and xml
find $RPM_BUILD_ROOT%{_docdir} -name '*.txt' -o -name '*.xml' | xargs %{__rm}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog MAINTAINERS README
%{_docdir}/xorg-docs
%{_mandir}/man7/Consortium.7*
%{_mandir}/man7/Standards.7*
%{_mandir}/man7/X.7*
%{_mandir}/man7/XOrgFoundation.7*
%{_mandir}/man7/XProjectTeam.7*
%{_mandir}/man7/Xsecurity.7*
