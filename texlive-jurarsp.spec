# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/jurarsp
# catalog-date 2007-01-08 14:12:54 +0100
# catalog-license gpl
# catalog-version 0.52
Name:		texlive-jurarsp
Version:	0.52
Release:	6
Summary:	Citations of judgements and official documents in (German) juridical documents
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/jurarsp
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jurarsp.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jurarsp.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jurarsp.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.52-2
+ Revision: 752940
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.52-1
+ Revision: 718764
- texlive-jurarsp
- texlive-jurarsp
- texlive-jurarsp
- texlive-jurarsp

