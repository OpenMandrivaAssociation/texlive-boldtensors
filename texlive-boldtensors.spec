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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides bold latin and greek characters within
\mathversion{normal}, by using ~ and " as active prefix characters.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/boldtensors
%dir %{_datadir}/texmf-dist/tex/latex/boldtensors
%doc %{_datadir}/texmf-dist/doc/latex/boldtensors/README.md
%doc %{_datadir}/texmf-dist/doc/latex/boldtensors/boldtensors.pdf
%doc %{_datadir}/texmf-dist/doc/latex/boldtensors/boldtensors.tex
%{_datadir}/texmf-dist/tex/latex/boldtensors/boldtensors.sty
%{_datadir}/texmf-dist/tex/latex/boldtensors/bt-isodiff.sty
