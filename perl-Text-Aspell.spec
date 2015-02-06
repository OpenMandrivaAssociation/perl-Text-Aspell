%define upstream_name    Text-Aspell
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	5

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


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.90.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-2mdv2011.0
+ Revision: 556157
- rebuild for perl 5.12

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.0
+ Revision: 405606
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.09-5mdv2009.0
+ Revision: 258610
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.09-4mdv2009.0
+ Revision: 246610
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.09-2mdv2008.1
+ Revision: 151407
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2008.1
+ Revision: 97571
- update to new version 0.09

* Wed Sep 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-2mdv2008.0
+ Revision: 90081
- rebuild

* Thu May 03 2007 Olivier Thauvin <nanardon@mandriva.org> 0.08-1mdv2008.0
+ Revision: 22120
- 0.08


* Tue Jul 11 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.06-1mdv2007.0
- New version 0.06

* Fri Apr 28 2006 Nicolas L�cureuil <neoclust@mandriva.org> 0.05-2mdk
- Fix SPEC according to Perl Policy
    - Source URL
- use mkrel

* Tue Aug 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdk
- New release 0.05
- fix URL source

* Tue Jun 07 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-3mdk 
- better url
- spec cleanup
- don't ship useless empty directories
- disable test, seems to be broken

* Mon Nov 15 2004 Michael Scherer <misc@mandrake.org> 0.04-2mdk
- Rebuild for new perl

* Wed Jun 30 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.04-1mdk 
- first mdk release

