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
Summary(es):	M�dulo de Perl Lingua::EN::Sentence
Summary(fr):	Module Perl Lingua::EN::Sentence
Summary(it):	Modulo di Perl Lingua::EN::Sentence
Summary(ja):	Lingua::EN::Sentence Perl �⥸�塼��
Summary(ko):	Lingua::EN::Sentence �� ����
Summary(no):	Perlmodul Lingua::EN::Sentence
Summary(pl):	Modu� Perla Lingua::EN::Sentence
Summary(pt):	M�dulo de Perl Lingua::EN::Sentence
Summary(pt_BR):	M�dulo Perl Lingua::EN::Sentence
Summary(ru):	������ ��� Perl Lingua::EN::Sentence
Summary(sv):	Lingua::EN::Sentence Perlmodul
Summary(uk):	������ ��� Perl Lingua::EN::Sentence
Summary(zh_CN):	Lingua::EN::Sentence Perl ģ��
Name:		perl-Lingua-EN-Sentence
Version:	0.23
Release:	2
License:	(enter GPL/LGPL/BSD/BSD-like/Artistic/other license name here)
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::EN::Sentence Perl module.

%description -l pl
Modu� Perla Lingua::EN::Sentence.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
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
%{perl_sitelib}/Lingua/EN/Sentence.pm
%{_mandir}/man3/*
