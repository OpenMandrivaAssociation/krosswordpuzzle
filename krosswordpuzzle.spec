Name:		krosswordpuzzle
Version:	0.15.6.2
Release:	%mkrel 2
License:	GPLv2+
URL:	        http://kde-apps.org/content/show.php/KrossWordPuzzle?content=111726
Group:		Games/Puzzles
Source0:	%name-%{version}.tar.gz
Summary:        %{name}- a crossword puzzle for KDE
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  kde4-macros
BuildRequires:  kdelibs4-devel
BuildRequires:  kdegames4-devel
BuildRequires:  qt4-devel
BuildRequires:  cmake

%description
This is a crossword playing game for KDE4. It can open *.puz-files
(AcrossLite) and it's own *.kwp-files (which are XML files).
You can download lots of crosswords from within the game.

%prep
%setup -q 

%build
cd %{name}
%cmake_kde4
%make

%install
rm -rf %buildroot
make -C %{name}/build DESTDIR=%buildroot install

%check
for f in %{buildroot}%{_kde_datadir}/applications/kde4/*.desktop ; do
     desktop-file-validate $f
done 

%find_lang %name

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%{_kde_bindir}/%{name}
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_datadir}/apps/%{name}/*
%{_kde_datadir}/config*
%{_kde_datadir}/doc/HTML/*
%{_kde_datadir}/mime/*
%{_kde_iconsdir}/*
