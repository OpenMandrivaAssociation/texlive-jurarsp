Name:		texlive-jurarsp
Version:	15878
Release:	1
Summary:	Citations of judgements and official documents in (German) juridical documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jurarsp
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jurarsp.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jurarsp.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jurarsp.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package should be helpful for people working on (German)
law. It (ab)uses BibTeX for citations of judgements and
official documents. For this purpose, a special BibTeX-style is
provided.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/jurarsp/jurarsp.bst
%{_texmfdistdir}/tex/latex/jurarsp/jurarsp.cfg
%{_texmfdistdir}/tex/latex/jurarsp/jurarsp.sty
%doc %{_texmfdistdir}/doc/latex/jurarsp/README
%doc %{_texmfdistdir}/doc/latex/jurarsp/jurarsp.pdf
%doc %{_texmfdistdir}/doc/latex/jurarsp/rsptest.bib
%doc %{_texmfdistdir}/doc/latex/jurarsp/rsptest.tex
#- source
%doc %{_texmfdistdir}/source/latex/jurarsp/jurarsp.dtx
%doc %{_texmfdistdir}/source/latex/jurarsp/jurarsp.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}
