# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-rjlparshap
Version:	20111104
Release:	4
Summary:	TeXLive rjlparshap package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rjlparshap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rjlparshap.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rjlparshap.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20111104-2
+ Revision: 755664
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20111104-1
+ Revision: 719454
- texlive-rjlparshap
- texlive-rjlparshap
- texlive-rjlparshap
- texlive-rjlparshap

