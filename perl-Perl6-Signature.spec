%define upstream_name    Perl6-Signature
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Parse, query, and pretty-print Perl 6 signatures
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Perl6/Perl6-Signature-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Moose)
BuildRequires:	perl(Parse::RecDescent)
BuildRequires:	perl(Test::Exception)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Balanced)
BuildArch:	noarch

%description
_Alpha release - everything here is subject to change_

*Perl6::Signature* models routine signatures as specified in Synopsis 6 of
the Perl 6 documentation. These signatures offer a rich language for
expressing type constraints, default values, and the optionality (among
other things) of routine parameters.

Included is a parser for the Signature language, accessors and convenience
methods for querying Signature objects, and a pretty-printer for producing
their canonical textual representation.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes 
%{_mandir}/man3/*
%{perl_vendorlib}/Perl6

%changelog
* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 404291
- rebuild using %%perl_convert_version

* Thu Dec 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2009.1
+ Revision: 310078
- import perl-Perl6-Signature


* Thu Dec 04 2008 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist


