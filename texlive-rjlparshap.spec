Name:		texlive-rjlparshap
Version:	15878
Release:	2
Summary:	TeXLive rjlparshap package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rjlparshap.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rjlparshap.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rjlparshap.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive rjlparshap package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rjlparshap/rjlpshap.sty
%doc %{_texmfdistdir}/doc/latex/rjlparshap/README
%doc %{_texmfdistdir}/doc/latex/rjlparshap/rjlpshap.pdf
#- source
%doc %{_texmfdistdir}/source/latex/rjlparshap/rjlpshap.dtx
%doc %{_texmfdistdir}/source/latex/rjlparshap/rjlpshap.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
