%define module  Text-Aspell
%define name    perl-%{module}
%define version 0.08
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Perl interface to the GNU Aspell library
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Text/%{module}-%{version}.tar.bz2
BuildRequires:  perl-devel
BuildRequires:  aspell-devel 
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module provides a Perl interface to the GNU Aspell library. The GNU Aspell
library provides access to system spelling libraries, including a spell
checker. This module is to meet the need of looking up many words, one at a
time, in a single session.

This is a Perl xs interface which should provide good performance compared to
forking the aspell program for every word.

%prep
%setup -q -n %{module}-%{version}

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

