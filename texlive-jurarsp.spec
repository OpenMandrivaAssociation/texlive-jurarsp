%global tl_name jurarsp
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.52
Release:	%{tl_revision}.1
Summary:	Citations of judgements and official documents in (German) juridical documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/jurarsp
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jurarsp.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jurarsp.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jurarsp.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package should be helpful for people working on (German) law. It
(ab)uses BibTeX for citations of judgements and official documents. For
this purpose, a special BibTeX-style is provided.

