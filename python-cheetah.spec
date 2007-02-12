Summary:	Python-powered template engine and code-generator
Summary(pl.UTF-8):   System szablonów dla języka Python
Name:		python-cheetah
Version:	1.0
Release:	3
License:	Python
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/cheetahtemplate/Cheetah-%{version}.tar.gz
# Source0-md5:	aaa4907b8877093b9bb11e6cea6b029b
Patch0:		%{name}-setuptools.patch
URL:		http://www.cheetahtemplate.org/
BuildRequires:	python >= 2.2.1
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	python-setuptools >= 0.6-0.a9.1
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python-powered template engine and code-generator.

%description -l pl.UTF-8
System szablonów dla języka Python.

%prep
%setup -q -n Cheetah-%{version}
%patch0 -p1

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
PYTHONPATH=$RPM_BUILD_ROOT%{py_sitedir}; export PYTHONPATH

python setup.py install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{py_sitedir}/Cheetah
%dir %{py_sitedir}/Cheetah/Templates
%dir %{py_sitedir}/Cheetah/Tests
%dir %{py_sitedir}/Cheetah/Tools
%dir %{py_sitedir}/Cheetah/Utils
%dir %{py_sitedir}/Cheetah/Utils/optik

%{py_sitedir}/Cheetah/*.py[oc]
%{py_sitedir}/Cheetah/*.so
%{py_sitedir}/Cheetah/Templates/*.py[oc]
%{py_sitedir}/Cheetah/Templates/*.tmpl
%{py_sitedir}/Cheetah/Tests/*.py[oc]
%{py_sitedir}/Cheetah/Tools/*.py[oc]
%{py_sitedir}/Cheetah/Utils/*.py[oc]
%{py_sitedir}/Cheetah/Utils/optik/*.py[oc]
%{py_sitedir}/Cheetah-1.0-py2.4.egg-info

%attr(755,root,root) %{_bindir}/cheetah
%attr(755,root,root) %{_bindir}/cheetah-compile
