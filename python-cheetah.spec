%define		_rc	a2
#
Summary:	Python-powered template engine and code-generator
Summary(pl):	System szablonów dla jêzyka Python
Name:		python-cheetah
Version:	0.9.16
Release:	1.%{_rc}.1
License:	Python
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/sourceforge/cheetahtemplate/Cheetah-%{version}%{_rc}.tar.gz
# Source0-md5:	e744fe28971a847f2ea56525e65e4896
URL:		http://www.cheetahtemplate.org/
BuildRequires:	python >= 2.2.1
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python-powered template engine and code-generator.

%description -l pl
System szablonów dla jêzyka Python.

%prep
%setup -q -n Cheetah-%{version}%{_rc}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
PYTHONPATH=$RPM_BUILD_ROOT%{py_sitedir}; export PYTHONPATH

python setup.py install \
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
%{py_sitedir}/Cheetah/Tests/*.py[oc]
%{py_sitedir}/Cheetah/Tools/*.py[oc]
%{py_sitedir}/Cheetah/Utils/*.py[oc]
%{py_sitedir}/Cheetah/Utils/optik/*.py[oc]

%attr(755,root,root) %{_bindir}/cheetah
%attr(755,root,root) %{_bindir}/cheetah-compile
