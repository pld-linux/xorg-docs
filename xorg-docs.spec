%if "%{_host_cpu}" == "x32"
%define	build_arch %{_target_platform}
%else
%define	build_arch %{_host}
%endif

Summary:	X.org documentation
Summary(pl.UTF-8):	Dokumentacja X.org
Name:		xorg-docs
Version:	1.7.3
Release:	1
License:	MIT
Group:		Documentation
Source0:	https://xorg.freedesktop.org/releases/individual/doc/%{name}-%{version}.tar.xz
# Source0-md5:	47399839f7f6cfb0c50610bad14eb4a9
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	tar >= 1:1.22
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.20
BuildRequires:	xz
Obsoletes:	xorg-docs-ps < 1.5
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
	--host=%{build_arch} \
	--build=%{build_arch} \
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
%doc ChangeLog MAINTAINERS README.md
%{_docdir}/xorg-docs
%{_mandir}/man7/Consortium.7*
%{_mandir}/man7/Standards.7*
%{_mandir}/man7/X.7*
%{_mandir}/man7/XOrgFoundation.7*
%{_mandir}/man7/XProjectTeam.7*
%{_mandir}/man7/Xsecurity.7*
