%include	/usr/lib/rpm/macros.python
Summary:	Python-powered template engine and code-generator
Summary(pl):	System szblonów dla jêzyka Python
Name:		python-cheetah
Version:	0.9.14
Release:	1
License:	Python license
Group:		Libraries/Python
Source0:	http://www.cheetahtemplate.org/Downloads/Cheetah-%{version}.tar.gz
URL:		http://www.cheetahtemplate.org/
BuildRequires:	python-devel >= 2.2.1
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python-powered template engine and code-generator.

%description -l pl
System szblonów dla jêzyka Python.

%prep
%setup -q -n Cheetah-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

PYTHONPATH=$RPM_BUILD_ROOT%{py_sitedir}
export PYTHONPATH

python setup.py install --optimize=2 --root=$RPM_BUILD_ROOT

gzip -9fn README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz

%dir %{py_sitedir}/Webware
%dir %{py_sitedir}/Webware/Cheetah
%{py_sitedir}/Webware/Cheetah/*.py[oc]
%{py_sitedir}/Webware/Cheetah/Templates/*.py[oc]
%{py_sitedir}/Webware/Cheetah/Tests/*.py[oc]
%{py_sitedir}/Webware/Cheetah/Tools/*.py[oc]
%{py_sitedir}/Webware/Cheetah/Utils/*.py[oc]

%{py_sitedir}/Webware.pth
