%define		_name	NiCo
Summary:	KDE icons - %{_name}
Summary(pl.UTF-8):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	0.1
Release:	1
License:	GPL
Group:		Themes
Source0:	http://ic3.deviantart.com/fs14/f/2007/095/4/3/%{_name}_Project_by_hammergom.zip
# Source0-md5:	da2f260cc03582b71eea43d843f24f98
URL:		http://www.deviantart.com/deviation/52511494/
Requires:	kdelibs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
%{_name} is icons theme for KDE.

%description -l pl.UTF-8
%{_name} to motyw ikon dla KDE.

%prep
%setup -q -n NiCo_Crystal
./buildset

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xfj NiCo_Project.tar.bz2 -C $RPM_BUILD_ROOT%{_iconsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/*
