Name:       harbour-newsapp

Summary:    An appication that needs a library
Version:    1
Release:    0
License:    LICENSE
URL:        http://example.org/
Source0:    %{name}-%{version}.tar.bz2
BuildRequires: newslib-devel
Requires:   newslib

%description
An application that needs a library

%prep
%setup -q -n %{name}-%{version}

%build
%qmake5 
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

%files
%defattr(-,root,root,-)
%{_bindir}
