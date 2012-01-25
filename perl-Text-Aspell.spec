%define upstream_name    Text-Aspell
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    Perl interface to the GNU Aspell library
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Text/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:  perl-devel
BuildRequires:  aspell-devel 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a Perl interface to the GNU Aspell library. The GNU Aspell
library provides access to system spelling libraries, including a spell
checker. This module is to meet the need of looking up many words, one at a
time, in a single session.

This is a Perl xs interface which should provide good performance compared to
forking the aspell program for every word.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
#make test

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorarch}/Text
%{perl_vendorarch}/auto/Text
%{_mandir}/*/*
