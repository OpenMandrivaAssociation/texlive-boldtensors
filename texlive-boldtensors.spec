Name:		texlive-boldtensors
Version:	15878
Release:	2
Summary:	Bold latin and greek characters through simple prefix characters
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/boldtensors
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boldtensors.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boldtensors.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
