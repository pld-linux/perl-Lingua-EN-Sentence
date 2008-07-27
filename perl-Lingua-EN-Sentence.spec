#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Lingua
%define		pnam	EN-Sentence
Summary:	Lingua::EN::Sentence Perl module
Summary(cs.UTF-8):	Modul Lingua::EN::Sentence pro Perl
Summary(da.UTF-8):	Perlmodul Lingua::EN::Sentence
Summary(de.UTF-8):	Lingua::EN::Sentence Perl Modul
Summary(es.UTF-8):	Módulo de Perl Lingua::EN::Sentence
Summary(fr.UTF-8):	Module Perl Lingua::EN::Sentence
Summary(it.UTF-8):	Modulo di Perl Lingua::EN::Sentence
Summary(ja.UTF-8):	Lingua::EN::Sentence Perl モジュール
Summary(ko.UTF-8):	Lingua::EN::Sentence 펄 모줄
Summary(nb.UTF-8):	Perlmodul Lingua::EN::Sentence
Summary(pl.UTF-8):	Moduł Perla Lingua::EN::Sentence
Summary(pt.UTF-8):	Módulo de Perl Lingua::EN::Sentence
Summary(pt_BR.UTF-8):	Módulo Perl Lingua::EN::Sentence
Summary(ru.UTF-8):	Модуль для Perl Lingua::EN::Sentence
Summary(sv.UTF-8):	Lingua::EN::Sentence Perlmodul
Summary(uk.UTF-8):	Модуль для Perl Lingua::EN::Sentence
Summary(zh_CN.UTF-8):	Lingua::EN::Sentence Perl 模块
Name:		perl-Lingua-EN-Sentence
Version:	0.25
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	4a846acfcb6eedd1c1557fc7f79f034d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lingua::EN::Sentence Perl module.

%description -l pl.UTF-8
Moduł Perla Lingua::EN::Sentence.

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
%{_mandir}/man3/*
