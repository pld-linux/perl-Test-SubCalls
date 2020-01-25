#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
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
Source0:	http://www.cpan.org/modules/by-module/Test/ADAMK/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	975a9fe8d93ef0298fc1bca8f03166e1
URL:		http://search.cpan.org/dist/Test-SubCalls/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.42
BuildRequires:	perl-Hook-LexWrap >= 0.20
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
Są różne sytuacje (jak testowanie kodu cache'ującego), kiedy chcemy
wykonać ileś testów, a następnie sprawdzić, że jakaś zagnieżdżona
procedura została wywołana ileś razy.

Ten moduł udostępnia funkcje do wykonywania takich testów w zwykłych
skryptach testowych Test::More (lub podobnych).

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
%{perl_vendorlib}/Test/SubCalls.pm
%{_mandir}/man3/Test::SubCalls.3pm*
