#
# Conditional build:
%bcond_without	ocaml_opt	# native optimized binaries (bytecode is always built)

# not yet available on x32 (ocaml 4.02.1), update when upstream will support it
%ifnarch %{ix86} %{x8664} %{arm} aarch64 ppc sparc sparcv9
%undefine	with_ocaml_opt
%endif

Summary:	Compatibility Result module for OCaml
Summary(pl.UTF-8):	Moduł zgodności Result dla OCamla
Name:		ocaml-result
Version:	1.5
Release:	1
License:	BSD
Group:		Libraries
#Source0Download: https://github.com/janestreet/result/releases
Source0:	https://github.com/janestreet/result/releases/download/%{version}/result-%{version}.tbz
# Source0-md5:	1b82dec78849680b49ae9a8a365b831b
URL:		https://github.com/janestreet/result
BuildRequires:	ocaml >= 1:4.00
BuildRequires:	ocaml-dune >= 1.0
%requires_eq	ocaml-runtime
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		debug_package	%{nil}

%description
Projects that want to use the new result type defined in OCaml >= 4.03
while staying compatible with older version of OCaml should use the
Result module defined in this library.

This package contains files needed to run bytecode executables using
Result library.

%description -l pl.UTF-8
Projekty chcące używać nowego typu result, zdefiniowanego w OCamlu 4.03
i nowszych, zachowując zgodność ze starszymi wersjami OCamla, powinny
używać modułu Result, zdefiniowanego w tej bibliotece.

Pakiet ten zawiera binaria potrzebne do uruchamiania programów
używających biblioteki Result.

%package devel
Summary:	Compatibility Result module for OCaml - development part
Summary(pl.UTF-8):	Moduł zgodności Result dla OCamla- cześć programistyczna
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%requires_eq	ocaml

%description devel
This package contains files needed to develop OCaml programs using
Result library.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki niezbędne do tworzenia programów używających
biblioteki Result.

%prep
%setup -q -n result-%{version}

%build
dune build --verbose

%install
rm -rf $RPM_BUILD_ROOT

dune install --destdir=$RPM_BUILD_ROOT

# sources
%{__rm} $RPM_BUILD_ROOT%{_libdir}/ocaml/result/result.ml
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/doc/result

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE.md README.md
%dir %{_libdir}/ocaml/result
%{_libdir}/ocaml/result/META
%{_libdir}/ocaml/result/result.cma
%if %{with ocaml_opt}
%attr(755,root,root) %{_libdir}/ocaml/result/result.cmxs
%endif

%files devel
%defattr(644,root,root,755)
%{_libdir}/ocaml/result/result.cmi
%{_libdir}/ocaml/result/result.cmt
%if %{with ocaml_opt}
%{_libdir}/ocaml/result/result.a
%{_libdir}/ocaml/result/result.cmx
%{_libdir}/ocaml/result/result.cmxa
%endif
%{_libdir}/ocaml/result/dune-package
%{_libdir}/ocaml/result/opam
