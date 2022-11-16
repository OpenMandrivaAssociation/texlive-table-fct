Name:		texlive-table-fct
Version:	41849
Release:	1
Summary:	Draw a variations table of functions and a convexity table of its graph
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/table-fct
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/table-fct.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/table-fct.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Draw a variations table of functions and a convexity table of
its graph This version offers two environnements, to draw
variations table of a function and a convexity table of its
graph.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/table-fct
%doc %{_texmfdistdir}/doc/latex/table-fct

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
