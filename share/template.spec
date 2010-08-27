%define upstream_name    DISTNAME
%define upstream_version DISTVERS

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    DISTSUMMARY
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DISTTOPLEVEL/%{upstream_name}-%{upstream_version}.DISTEXTENSION

DISTBUILDREQUIRES
DISTARCH
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
DISTDESCR

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
DISTBUILDBUILDER
DISTMAKER

%check
DISTMAKER test

%install
rm -rf %buildroot
DISTINSTALL

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
DISTDOC
%{_mandir}/man3/*
%perl_vendorlib/*
DISTEXTRA

%changelog
* DISTDATE cpan2dist DISTVERS-1mdv
- initial mdv release, generated with cpan2dist
