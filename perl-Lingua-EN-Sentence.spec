#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Lingua
%define		pnam	EN-Sentence
Summary:	Lingua::EN::Sentence Perl module
Summary(cs):	Modul Lingua::EN::Sentence pro Perl
Summary(da):	Perlmodul Lingua::EN::Sentence
Summary(de):	Lingua::EN::Sentence Perl Modul
Summary(es):	Módulo de Perl Lingua::EN::Sentence
Summary(fr):	Module Perl Lingua::EN::Sentence
Summary(it):	Modulo di Perl Lingua::EN::Sentence
Summary(ja):	Lingua::EN::Sentence Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Lingua::EN::Sentence ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Lingua::EN::Sentence
Summary(pl):	Modu³ Perla Lingua::EN::Sentence
Summary(pt):	Módulo de Perl Lingua::EN::Sentence
Summary(pt_BR):	Módulo Perl Lingua::EN::Sentence
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Lingua::EN::Sentence
Summary(sv):	Lingua::EN::Sentence Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Lingua::EN::Sentence
Summary(zh_CN):	Lingua::EN::Sentence Perl Ä£¿é
Name:		perl-Lingua-EN-Sentence
Version:	0.25
Release:	2
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4a846acfcb6eedd1c1557fc7f79f034d
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::EN::Sentence Perl module.

%description -l pl
Modu³ Perla Lingua::EN::Sentence.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{!?_without_tests:%{__make} test}

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
%{_mandir}/man3/*
