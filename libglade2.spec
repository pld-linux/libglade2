# register glade-2.0.dtd
Summary:	libglade library
Summary(es):	El libglade permite que usted cargue archivos del interfaz del glade
Summary(pl):	Biblioteka do ³adowania definicji interfejsu generowanego programem glade
Summary(pt_BR):	Esta biblioteca permite carregar arquivos da interface glade
Name:		libglade2
Version:	2.0.1
Release:	2
Epoch:		1
License:	LGPL
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME//sources/libglade/2.0/libglade-%{version}.tar.bz2
Patch0:		%{name}-xmldoc.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	gettext-devel
BuildRequires:	bison
BuildRequires:	gtk+2-devel >= 2.0.6
BuildRequires:	libxml2-devel >= 2.4.24
BuildRequires:	glib2-devel >= 2.0.6
BuildRequires:	gtk-doc >= 0.9-4
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libglade2.0

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_gtkdocdir	%{_defaultdocdir}/gtk-doc/html

%description
This library allows you to load user interfaces in your program, which
are stored externally. This allows alteration of the interface without
recompilation of the program. The interfaces can also be edited with
GLADE.

%description -l es
El libglade permite que usted cargue archivos del interfaz del glade
en tiempo de ejecución.

%description -l pl
Biblioteka libglade umo¿liwia dynamiczne ³adowanie definicji
interfejsu u¿ytkownika generowanego za pomoc± programu glade. Taka
separacja definicji interfejsu umo¿liwia pracê nad nim bez
konieczno¶ci rekompilacji programu.

%description -l pt_BR
O libglade permite carregar, em tempo de execução, arquivos da
interface glade. Não é necessário ter o glade instalado, mas esta é a
melhor maneira de criar os arquivos de interface.

%package devel
Summary:	Libraries, includes, etc to develop libglade applications
Summary(es):	Archivos necesarios para el desarrollo de aplicaciones con libglade
Summary(pl):	Biblioteki, pliki nag³ówkowe i dokumentacja dla programisty
Summary(pt_BR):	Arquivos necessários para o desenvolvimento de aplicações com a interface glade
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	libxml2-devel
Requires:	gtk+2-devel >= 2.0.0
Requires:	gtk-doc-common
Obsoletes:	libglade2.0-devel

%description devel
Libraries, include files, etc you can use to develop libglade
applications.

%description devel -l es
Archivos de inclusión y bibliotecas necesarias para el desarrollo de
aplicaciones con glade.

%description devel -l pl
Biblioteki, pliki nag³ówkowe i dokumentacja dla programisty.

%description devel -l pt_BR
Arquivos de inclusão e bibliotecas para o desenvolvimento de
aplicações com a interface glade.

%package static
Summary:	Static libglade library
Summary(es):	Archivos estáticos necesarios para el desarrollo de aplicaciones con libglade
Summary(pl):	Biblioteka statyczna libglade
Summary(pt_BR):	Arquivos estáticos necessários para o desenvolvimento de aplicações com a interface glade
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libglade library.

%description static -l es
Archivos estáticos necesarias para el desarrollo de aplicaciones con
glade.

%description static -l pl
Biblioteka statyczna libglade.

%description static -l pt_BR
Bibliotecas estáticas para o desenvolvimento de aplicações com a
interface glade.

%prep
%setup -q -n libglade-%{version}
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
glib-gettextize --copy --force
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk-doc \
	--with-html-path=%{_gtkdocdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/libglade/2.0

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir} \
	pkgconfigdir=%{_pkgconfigdir}


%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_libdir}/libglade
%{_datadir}/xml/libglade/*.dtd

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_pkgconfigdir}/*
%{_includedir}/libglade-*
%{_gtkdocdir}/libglade

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
