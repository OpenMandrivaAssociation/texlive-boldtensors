Name:		texlive-boldtensors
Version:	20080817
Release:	1
Summary:	Bold latin and greek characters through simple prefix characters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/boldtensors
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boldtensors.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boldtensors.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
This package provides bold latin and greek characters within
\mathversion{normal}, by using ~ and " as prefix characters.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
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
