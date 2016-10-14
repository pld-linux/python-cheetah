Summary:	Python-powered template engine and code-generator
Summary(pl.UTF-8):	System szablonów dla języka Python
Name:		python-cheetah
Version:	2.4.4
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/simple/cheetah/
Source0:	https://files.pythonhosted.org/packages/source/C/Cheetah/Cheetah-%{version}.tar.gz
# Source0-md5:	853917116e731afbc8c8a43c37e6ddba
URL:		http://www.cheetahtemplate.org/
BuildRequires:	python >= 2.2.1
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	python-markdown >= 2.0.1
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
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
%doc CHANGES LICENSE README.markdown TODO
%attr(755,root,root) %{_bindir}/cheetah
%attr(755,root,root) %{_bindir}/cheetah-analyze
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
%{py_sitedir}/Cheetah-%{version}-py*.egg-info
