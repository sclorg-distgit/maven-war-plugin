%global pkg_name maven-war-plugin
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.3
Release:        9.11%{?dist}
Summary:        Maven WAR Plugin

License:        ASL 2.0
URL:            http://maven.apache.org/plugins/maven-war-plugin/
Source0:        http://repo2.maven.org/maven2/org/apache/maven/plugins/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip

BuildArch: noarch

# Basic stuff
BuildRequires: %{?scl_prefix_java_common}javapackages-tools
# Maven and its dependencies
BuildRequires: %{?scl_prefix_java_common}maven-local
BuildRequires: maven30-maven-plugin-plugin
BuildRequires: maven30-maven-javadoc-plugin
BuildRequires: maven30-maven-jar-plugin
BuildRequires: maven30-maven-surefire-provider-junit
BuildRequires: maven30-maven-surefire-plugin
BuildRequires: maven30-maven-filtering
BuildRequires: maven30-maven-enforcer-plugin
BuildRequires: maven30-maven-compiler-plugin
BuildRequires: maven30-maven-install-plugin
BuildRequires: maven30-maven-resources-plugin
BuildRequires: maven30-maven-changes-plugin
# Others
BuildRequires: maven30-xstream



%description
Builds a Web Application Archive (WAR) file from the project output and its 
dependencies.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{version}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%dir %{_mavenpomdir}/%{pkg_name}
%dir %{_javadir}/%{pkg_name}
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 2.3-9.11
- maven33 rebuild

* Thu Jan 15 2015 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-9.10
- Add directory ownership on %%{_mavenpomdir} subdir

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 2.3-9.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 2.3-9.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-9.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-9.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-9.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-9.4
- Remove requires on java

* Fri Feb 14 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-9.3
- SCL-ize requires and build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-9.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-9.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.3-9
- Mass rebuild 2013-12-27

* Fri Aug 23 2013 Michal Srb <msrb@redhat.com> - 2.3-8
- Migrate away from mvn-rpmbuild (Resolves: #997493)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Apr 29 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.3-6
- Remove unneeded BR: maven-idea-plugin

* Thu Feb 28 2013 Weinan Li <weli@redhat.com> 2.3-5
- Remove unnecessary maven-doxia dependencies

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.3-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Fri Nov 23 2012 Weinan Li <weli@redhat.com> 2.3-2
- Install license files

* Tue Oct 23 2012 Alexander Kurtakov <akurtako@redhat.com> 2.3-1
- Update to latest upstream release.

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Mar 5 2012 Alexander Kurtakov <akurtako@redhat.com> 2.2-1
- Update to latest release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Jun 17 2011 Alexander Kurtakov <akurtako@redhat.com> 2.1.1-4
- Do not depend on maven2.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jan 26 2011 Alexander Kurtakov <akurtako@redhat.com> 2.1.1-2
- Build with maven 3.
- Drop depmap and other non needed parts.

* Sat Nov 20 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1.1-1
- Update to new version.

* Mon Jun 14 2010 Alexander Kurtakov <akurtako@redhat.com> 2.1-0.3.b1
- Fix unversioned symlink.

* Mon Jun 7 2010 Weinan Li <weli@redhat.com> - 2.1-0.2.b1
- Fix incoherent version in changelog

* Thu Jun 3 2010 Weinan Li <weli@redhat.com> - 2.1-0.1.b1
- Initial Package
