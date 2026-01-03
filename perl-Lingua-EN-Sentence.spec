#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Lingua
%define		pnam	EN-Sentence
Summary:	Lingua::EN::Sentence Perl module - splitting text into sentences
Summary(pl.UTF-8):	Moduł Perla Lingua::EN::Sentence - podział tekstu na zdania
Name:		perl-Lingua-EN-Sentence
Version:	0.34
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/modules/by-module/Lingua/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0e111dce8f97dd6060d2b2683739e4d4
URL:		https://search.cpan.org/dist/Lingua-EN-Sentence/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Lingua::EN::Sentence Perl module contains the function
get_sentences, which splits text into its constituent sentences, based
on a regular expression and a list of abbreviations (built in and
given).

%description -l pl.UTF-8
Moduł Perla Lingua::EN::Sentence zawiera funkcję get_sentences,
dzielącą tekst na zdania składowe, w oparciu o wyrażenie regularne i
listę skrótów (wbudowaną oraz podaną).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Lingua/EN/Sentence.pm
%{_mandir}/man3/Lingua::EN::Sentence.3pm*
