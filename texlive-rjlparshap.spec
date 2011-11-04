# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-rjlparshap
Version:	20111104
Release:	1
Summary:	TeXLive rjlparshap package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rjlparshap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rjlparshap.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rjlparshap.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
TeXLive rjlparshap package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/rjlparshap/rjlpshap.sty
%doc %{_texmfdistdir}/doc/latex/rjlparshap/README
%doc %{_texmfdistdir}/doc/latex/rjlparshap/rjlpshap.pdf
#- source
%doc %{_texmfdistdir}/source/latex/rjlparshap/rjlpshap.dtx
%doc %{_texmfdistdir}/source/latex/rjlparshap/rjlpshap.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
