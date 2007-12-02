# TODO
# - main.o(.text+0x976): In function `create_file_names':
#   main.c: warning: the use of `mktemp' is dangerous, better use `mkstemp'
Summary:	Parser Generator with Java Extension
Name:		byaccj
Version:	1.14
Release:	0.1
License:	GPL
Group:		Development/Languages/Java
URL:		http://byaccj.sourceforge.net/
Source0:	http://dl.sourceforge.net/byaccj/%{name}%{version}_src.tar.gz
# Source0-md5:	23c7d0526a3794f06635f3ef3845a045
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
BYACC/J is an extension of the Berkeley v 1.8 YACC-compatible parser
generator. Standard YACC takes a YACC source file, and generates one
or more C files from it, which if compiled properly, will produce a
LALR-grammar parser. This is useful for expression parsing,
interactive command parsing, and file reading. Many megabytes of YACC
code have been written over the years. This is the standard YACC tool
that is in use every day to produce C/C++ parsers. I have added a "-J"
flag which will cause BYACC to generate Java source code, instead. So
there finally is a YACC for Java now!

%prep
%setup -q -n %{name}%{version}_src

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
%doc docs/*
%attr(755, root, root) %{_bindir}/%{name}
