Name: hunspell-sc
Summary: Sardinian hunspell dictionaries
%define upstreamid 20081101
Version: 0.%{upstreamid}
Release: 11%{?dist}
Group: Applications/Text
Source: http://extensions.services.openoffice.org/files/1446/2/Dict_sc_IT03.oxt
URL: http://extensions.services.openoffice.org/project/Dict_sc
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#The license included is AGPLv3 and pkg-desc/pkg-description.txt
#says AGPLv3 or later, but the sc_IT.aff header states "GPLv2"
License: AGPLv3+ and GPLv2
BuildArch: noarch
BuildRequires: hunspell-devel

Requires: hunspell

%description
Sardinian hunspell dictionaries.

%prep
%setup -q -c -n hunspell-sc

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p sc_IT.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/sc_IT.aff
cp -p sc_it.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/sc_IT.dic

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc registration/agpl3-en.txt
%{_datadir}/myspell/*

%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.20081101-11
- Mass rebuild 2013-12-27

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081101-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Dec 11 2012 Caolan McNamara <caolanm@redhat.com> - 0.20081101-9
- liblangtag detected that the .dic here has an incorrect lowercase territory

* Tue Nov 06 2012 Caolan McNamara <caolanm@redhat.com> - 0.20081101-8
- clarify license

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081101-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081101-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081101-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081101-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 09 2009 Caolan McNamara <caolanm@redhat.com> - 0.20081101-3
- drop unneeded buildrequires

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081101-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Nov 28 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081101-1
- latest version

* Wed Oct 29 2008 Caolan McNamara <caolanm@redhat.com> - 0.20081027-1
- initial version
