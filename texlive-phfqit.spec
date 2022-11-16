Name:		texlive-phfqit
Version:	60734
Release:	1
Summary:	Macros for typesetting Quantum Information Theory
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/phfqit
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfqit.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfqit.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phfqit.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides macros to typeset some general
mathematical operators (identity operator, trace, diagonal,
rank, ...), a powerful implementation of the bra-ket notation
(kets, bras, brakets, matrix elements etc. which can be sized
as required), delimited expressions such as averages and norms,
and some basic Lie algebra/group names. Macros for entropy
measures for quantum information theory (smooth min- and
max-entropy, smooth relative entropies, etc.) are also
provided.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/phfqit
%{_texmfdistdir}/tex/latex/phfqit
%doc %{_texmfdistdir}/doc/latex/phfqit

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
