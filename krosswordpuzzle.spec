%define svn 1327226

Name:		krosswordpuzzle
Version:	0.16
%if 0%svn
Release:	0.%svn.1
Source0:	%name-%svn.tar.xz
%else
Release:	2
Source0:	%name-%{version}.tar.gz
%endif
Patch0:		krosswordpuzzle-compile.patch
License:	GPLv2+
URL:	        http://kde-apps.org/content/show.php/KrossWordPuzzle?content=111726
Group:		Games/Puzzles
Summary:        %{name}- a crossword puzzle for KDE

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
%if 0%svn
%setup -q -n %name-%svn
%else
%setup -q
%endif
%autopatch -p1

%build
%cmake_kde4
%make

%install
rm -rf %buildroot
make -C build DESTDIR=%buildroot install

%check
for f in %{buildroot}%{_kde_datadir}/applications/kde4/*.desktop ; do
     desktop-file-validate $f
done 

%find_lang %name || touch %name.lang

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%{_kde_bindir}/%{name}
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_datadir}/apps/%{name}/*
%{_kde_datadir}/config*
%optional %{_kde_datadir}/doc/HTML/*
%{_kde_datadir}/mime/*
%{_kde_iconsdir}/*
%_kde_libdir/kde4/crosswordthumbnail.so
%_kde_datadir/kde4/services/crosswordthumbnail.desktop


%changelog
* Tue May 11 2010 Caio Begotti <caio1982@mandriva.org> 0.15.6.2-1mdv2010.1
+ Revision: 544531
- import krosswordpuzzle

