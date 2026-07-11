%global tl_name phfqit
%global tl_revision 60734

Name:		texlive-%{tl_name}
Epoch:		1
Version:	4.1
Release:	%{tl_revision}.1
Summary:	Macros for typesetting Quantum Information Theory
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/phfqit
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phfqit.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phfqit.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phfqit.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides macros to typeset some general mathematical
operators (identity operator, trace, diagonal, rank, ...), a powerful
implementation of the bra-ket notation (kets, bras, brakets, matrix
elements etc. which can be sized as required), delimited expressions
such as averages and norms, and some basic Lie algebra/group names.
Macros for entropy measures for quantum information theory (smooth min-
and max-entropy, smooth relative entropies, etc.) are also provided.

