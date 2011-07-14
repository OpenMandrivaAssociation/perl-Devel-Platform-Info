%define upstream_name    Devel-Platform-Info
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Retrieve Solaris platform metadata
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Devel/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(IO::File)
BuildRequires: perl(Test::Builder::Tester)
BuildRequires: perl(Test::More) >= 0.700.0
BuildArch:  noarch

%description
This module is a wrapper to the drivers which can determine platform
metadata regarding the currently running operating system.

The intention of this distribution is to provide key identifying components
regarding the platform currently being used, for the CPAN Testers test
reports. Currently the reports do not often contain enough information to
help authors understand specific failures, where the platform may be a
factor.

However, it is hoped that this distribution will find more uses far beyond
the usage for CPAN Testers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.json META.yml README examples
%{_mandir}/man3/*
%perl_vendorlib/*
