Summary:	Parser Generator with Java Extension
Summary(pl.UTF-8):	Generator analizatorów rozszerzony o Javę
Name:		byaccj
Version:	1.15
Release:	2
License:	Public Domain
Group:		Development/Languages/Java
Source0:	http://dl.sourceforge.net/byaccj/%{name}%{version}_src.tar.gz
# Source0-md5:	5ee9959af35f245ac2c4355f85fdf351
Patch0:		%{name}-cflags.patch
Patch1:		%{name}-mkstemp.patch
URL:		http://byaccj.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BYACC/J is an extension of the Berkeley v 1.8 YACC-compatible parser
generator. Standard YACC takes a YACC source file, and generates one
or more C files from it, which if compiled properly, will produce a
LALR-grammar parser. This is useful for expression parsing,
interactive command parsing, and file reading. Many megabytes of YACC
code have been written over the years. This is the standard YACC tool
that is in use every day to produce C/C++ parsers, but it has added a
"-J" flag which will cause BYACC to generate Java source code,
instead. So there finally is a YACC for Java now!

%description -l pl.UTF-8
BYACC/J to rozszerzenie generatora analizatorów kompatybilnego z
Berkeley YACC 1.8. Standardowy YACC pobiera plik źródłowy YAC i tworzy
z niego jeden lub więcej plików C, które po skompilowaniu tworzą
analizator gramatyki LALR. Jest on przydatny do analizy wyrażeń,
analizy interaktywnych poleceń oraz czytania plików. Na przestrzeni
lat powstało wiele megabajtów kodu YACC. Ten pakiet zawiera
standardowe narzędzie YACC używane na co dzień do tworzenia
analizatorów C/C++, ale ma dodaną flagę "-J", która powoduje
generowanie kodu źródłowego w Javie zamiast C/C++. W ten sposób
powstał YACC dla Javy.

%prep
%setup -q -n %{name}%{version}

%patch -P0 -p1
%patch -P1 -p1

%build
%{__make} -C src linux \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install src/yacc.linux $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/* src/{new_features,no_warranty}
%attr(755,root,root) %{_bindir}/%{name}
