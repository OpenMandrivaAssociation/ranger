Name:           ranger
Version:        1.9.2
Release:        1
Summary:        A flexible console file manager

Group:          File tools
License:        GPLv3+
URL:            https://ranger.github.io/
Source0:        https://github.com/ranger/ranger/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
Requires:	python-chardet
Requires:	sudo

#Suggests:       w3m-img

%description
Ranger is a free console file manager that gives you greater flexibility and a
good overview of your files without having to leave your *nix console. It
visualizes the directory tree in two dimensions: the directory hierarchy on
one, lists of files on the other, with a preview to the right so you know where
you'll be going.

%prep
%setup -q

%build
%py3_build


%install
%{__python3} setup.py install -O1 --skip-build --root %{buildroot}
mv %{buildroot}%{_docdir}/%{name} rpmdocs
find rpmdocs -type f -exec chmod -v -R -X '{}' \;
sed -i 's!python -s -O!python -O!g' %{buildroot}%{_bindir}/%{name}


%files
%doc rpmdocs/*
%{_bindir}/ranger
%{_bindir}/rifle
%{_datadir}/applications/%{name}.desktop
%{python3_sitelib}/*
%{_mandir}/man1/ranger.1.*
%{_mandir}/man1/rifle.1.*
