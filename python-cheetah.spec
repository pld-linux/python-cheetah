Summary:	Python-powered template engine and code-generator
Summary(pl.UTF-8):	System szablonów dla języka Python
Name:		python-cheetah
Version:	2.2.1
Release:	3
License:	MIT
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/cheetahtemplate/Cheetah-%{version}.tar.gz
# Source0-md5:	137491aef378b502b2ee71c03b929faf
URL:		http://www.cheetahtemplate.org/
BuildRequires:	python >= 2.2.1
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python-powered template engine and code-generator.

%description -l pl.UTF-8
System szablonów dla języka Python.

%prep
%setup -q -n Cheetah-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE README TODO
%attr(755,root,root) %{_bindir}/cheetah
%attr(755,root,root) %{_bindir}/cheetah-compile
%dir %{py_sitedir}/Cheetah
%{py_sitedir}/Cheetah/*.py[oc]
%attr(755,root,root) %{py_sitedir}/Cheetah/_namemapper.so
%dir %{py_sitedir}/Cheetah/Macros
%{py_sitedir}/Cheetah/Macros/*.py[oc]
%dir %{py_sitedir}/Cheetah/Templates
%{py_sitedir}/Cheetah/Templates/*.py[oc]
%{py_sitedir}/Cheetah/Templates/*.tmpl
%dir %{py_sitedir}/Cheetah/Tests
%{py_sitedir}/Cheetah/Tests/*.py[oc]
%dir %{py_sitedir}/Cheetah/Tools
%{py_sitedir}/Cheetah/Tools/*.py[oc]
%{py_sitedir}/Cheetah/Tools/*.txt
%dir %{py_sitedir}/Cheetah/Utils
%{py_sitedir}/Cheetah/Utils/*.py[oc]
%dir %{py_sitedir}/Cheetah/contrib
%{py_sitedir}/Cheetah/contrib/*.py[oc]
%dir %{py_sitedir}/Cheetah/contrib/markdown
%{py_sitedir}/Cheetah/contrib/markdown/*.py[oc]
%{py_sitedir}/Cheetah-*.egg-info
