%global tl_name boldtensors
%global tl_revision 79183

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Bold latin and greek characters through simple prefix characters
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/boldtensors
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/boldtensors.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/boldtensors.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides bold latin and greek characters within
\mathversion{normal}, by using ~ and " as active prefix characters.

