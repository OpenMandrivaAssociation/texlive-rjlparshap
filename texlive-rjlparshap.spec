%global tl_name rjlparshap
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Support for use of \parshape in LaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rjlparshap
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rjlparshap.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rjlparshap.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rjlparshap.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides macros and environments that relieve the programmer
of some of the difficulties of using \parshape in LaTeX macros. It does
not actually calculate shapes in the way that the shapepar package does.

