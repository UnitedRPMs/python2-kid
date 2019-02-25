Name:           python2-kid
Version:        0.9.6
Release:        23%{?dist}
Summary:        Kid - A simple and pythonic XML template language

Group:          Applications/Publishing
License:        MIT
URL:            http://www.kid-templating.org/
Source0:        https://files.pythonhosted.org/packages/85/59/5256812b4b90cf379be2947142aa384f0b2f739643933ffab66914c79332/kid-%{version}.tar.gz
# 2010-01-10: Upstream is currently unresponsive, but patch qualifies for upstreaming
# Escape ]]> to ]]&gt; in serialization.py as required by XML standard:
# http://www.w3.org/TR/2006/REC-xml11-20060816/#syntax
# Red Hat Bugzilla: https://bugzilla.redhat.com/show_bug.cgi?id=528729
Patch0:         python-kid-0.9.6-escape-gt.patch
BuildArch:      noarch

BuildRequires:  python2-devel 
BuildRequires:  python2-docutils
%{?python_provide:%python_provide python2-kid}


%description 

Kid is a simple Python based template language for generating and
transforming XML vocabularies. Templates are compiled to native Python
byte-code and may be imported and used like normal Python modules.



%prep
%setup -q -n kid-%{version}
%patch0 -p1 -b .escape-gt


%build
%py2_build


%install
rm -rf $RPM_BUILD_ROOT
%{__python2} setup.py install --skip-build --root $RPM_BUILD_ROOT \
    --single-version-externally-managed
rm -rf $RPM_BUILD_ROOT%{python2_sitelib}/kid/test
rm -f $RPM_BUILD_ROOT%{python2_sitelib}/*egg-info/requires.txt
# Avoid requiring setuptools
chmod 0755 $RPM_BUILD_ROOT%{python2_sitelib}/kid/{run,compile}.py
rm -f $RPM_BUILD_ROOT%{_bindir}/*
ln -s ../..%{python2_sitelib}/kid/run.py $RPM_BUILD_ROOT%{_bindir}/kid
ln -s ../..%{python2_sitelib}/kid/compile.py $RPM_BUILD_ROOT%{_bindir}/kidc

# Mangle fix

sed -i 's|/usr/bin/env python|/usr/bin/python2|g' $RPM_BUILD_ROOT/%{python2_sitelib}/kid/compile.py
sed -i 's|/usr/bin/env python|/usr/bin/python2|g' $RPM_BUILD_ROOT/%{python2_sitelib}/kid/run.py


%files 
%license COPYING
%doc HISTORY README doc/*.txt doc/*.css test
%{python2_sitelib}/kid*
%{_bindir}/*


%changelog
* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.9.6-21
- Python 2 binary package renamed to python2-kid
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 09 2017 Iryna Shcherbina <ishcherb@redhat.com> - 0.9.6-20
- Add a build-time dependency on python2-devel

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-17
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.6-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 12 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.9.6-13
- Replace BR on python-setuptools-devel with python-setuptools

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.9.6-7
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jan 10 2010 Till Maas <opensource@till.name> - 0.9.6-6
- Escape ]]> as ]]&gt; in serialization.py to create valid XML
- https://bugzilla.redhat.com/show_bug.cgi?id=528729

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.9.6-3
- Rebuild for Python 2.6

* Tue Aug 28 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.6-2
- BR: python-setuptools-devel
- Drop explicit BR: python-devel

* Fri Aug 17 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.6-1
- Upstream 0.9.6

* Sun Jan 28 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.5-1
- Upstream 0.9.5
- Drop the py-def patch

* Tue Jan 02 2007 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.4-2
- Add hotfix for broken py-def (#220843)
- Simplify kid and kidc to not require setuptools to run (#220844)

* Sun Dec 17 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.4-1
- Version 0.9.4
- Ghostbusting

* Sun Jul 23 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.3-1
- Version 0.9.3
- Adjusting urls to point to kid-templating.org

* Tue Jun 27 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.2-1
- Version 0.9.2
- BR python-setuptools >= 0.6a11

* Tue May 23 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.1-3
- Fix 'elementtree requried' regression

* Sat May 20 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.1-2
- Update project URL

* Fri May 19 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9.1-1
- Version 0.9.1

* Mon Feb 27 2006 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.9-1
- Version 0.9
- Switch to using setuptools.
- Handle .egg data.
- Don't list python-abi namely -- FC4 and above does it automatically.

* Fri Dec 02 2005 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.8-1
- Version 0.8

* Fri Nov 11 2005 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.7.1-2
- Rebuild.

* Thu Nov 10 2005 Konstantin Ryabitsev <icon@fedoraproject.org> - 0.7.1-1
- Version 0.7.1
- Avoid setuptools using a patch to use standard distutils
- Avoid cruft in doc dir

* Mon Jun 13 2005 Konstantin Ryabitsev <icon@linux.duke.edu> - 0.6.4-1
- Version 0.6.4
- Disttagging

* Sat Apr 16 2005 Seth Vidal <skvidal at phy.duke.edu> 0.6.3-2
- BuildRequires python-elementtree

* Tue Mar 29 2005 Konstantin Ryabitsev <icon@linux.duke.edu> 0.6.3-2
- Add docs and list files instead of using INSTALLED_FILES (safer)
- Trim description a little
- Require python-abi
- BuildRequire python-devel
- Use python_sitelib
- Remove test directory from site_packages
- Use ghosting for .pyo

* Mon Mar 14 2005 Konstantin Ryabitsev <icon@linux.duke.edu> 0.6.3-1
- Version 0.6.3

* Thu Mar 10 2005 Konstantin Ryabitsev <icon@linux.duke.edu> 0.6.2-1
- Initial build in Fedora Extras format.
