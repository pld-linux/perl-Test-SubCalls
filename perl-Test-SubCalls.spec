#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Test
%define	pnam	SubCalls
Summary:	Test::SubCalls - Track the number of times subs are called
Summary(pl.UTF-8):	Test::SubCalls - śledzi liczbę razy ile został wywołany podprogram
Name:		perl-Test-SubCalls
Version:	1.09
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	975a9fe8d93ef0298fc1bca8f03166e1
URL:		http://search.cpan.org/dist/Test-SubCalls/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Hook::LexWrap) >= 0.20
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
There are a number of different situations (like testing caching code)
where you want to want to do a number of tests, and then verify that
some underlying subroutine deep within the code was called a specific
number of times.

This module provides a number of functions for doing testing in this
way in association with your normal Test::More (or similar) test
scripts.

%description -l pl.UTF-8
Moduł ten śledzi liczbę razy ile został wywołany podprogram.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/*.pm
%{_mandir}/man3/*
