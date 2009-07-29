%define upstream_name    Perl6-Signature
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Parse, query, and pretty-print Perl 6 signatures
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Perl6/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Moose)
BuildRequires: perl(Parse::RecDescent)
BuildRequires: perl(Test::Exception)
BuildRequires: perl(Test::More)
BuildRequires: perl(Text::Balanced)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/Perl6
