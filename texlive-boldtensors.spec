# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/boldtensors
# catalog-date 2008-08-17 01:00:50 +0200
# catalog-license gpl
# catalog-version undef
Name:		texlive-boldtensors
Version:	20170414
Release:	1
Summary:	Bold latin and greek characters through simple prefix characters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/boldtensors
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boldtensors.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boldtensors.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides bold latin and greek characters within
\mathversion{normal}, by using ~ and " as prefix characters.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/boldtensors/boldtensors.sty
%doc %{_texmfdistdir}/doc/latex/boldtensors/boldtensors.pdf
%doc %{_texmfdistdir}/doc/latex/boldtensors/boldtensors.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20080817-2
+ Revision: 749798
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20080817-1
+ Revision: 717962
- texlive-boldtensors
- texlive-boldtensors
- texlive-boldtensors
- texlive-boldtensors
- texlive-boldtensors

