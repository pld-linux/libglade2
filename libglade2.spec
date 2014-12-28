#
# TODO: register glade-2.0.dtd
#
# Conditional build:
%bcond_without	apidocs		# disable gtk-doc
#
Summary:	libglade library
Summary(es.UTF-8):	El libglade permite que usted cargue archivos del interfaz del glade
Summary(pl.UTF-8):	Biblioteka do ładowania definicji interfejsu generowanego programem glade
Summary(pt_BR.UTF-8):	Esta biblioteca permite carregar arquivos da interface glade
Name:		libglade2
Version:	2.6.4
Release:	7
Epoch:		1
License:	LGPL v2+
Group:		X11/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/libglade/2.6/libglade-%{version}.tar.bz2
# Source0-md5:	d1776b40f4e166b5e9c107f1c8fe4139
URL:		http://www.gnome.org/
BuildRequires:	atk-devel >= 1:1.18.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.9
BuildRequires:	bison
BuildRequires:	docbook-dtd412-xml
BuildRequires:	gettext-tools
BuildRequires:	gnome-common
BuildRequires:	gtk+2-devel >= 2:2.10.13
%{?with_apidocs:BuildRequires:	gtk-doc >= 1.8}
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.29
BuildRequires:	pkgconfig
BuildRequires:	python >= 2.0
BuildRequires:	python-modules >= 2.0
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.197
Requires:	FHS >= 2.3-16
Requires:	atk >= 1:1.18.0
Requires:	python-modules >= 2.0
Obsoletes:	libglade2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library allows you to load user interfaces in your program, which
are stored externally. This allows alteration of the interface without
recompilation of the program. The interfaces can also be edited with
GLADE.

%description -l es.UTF-8
El libglade permite que usted cargue archivos del interfaz del glade
en tiempo de ejecución.

%description -l pl.UTF-8
Biblioteka libglade umożliwia dynamiczne ładowanie definicji
interfejsu użytkownika generowanego za pomocą programu glade. Taka
separacja definicji interfejsu umożliwia pracę nad nim bez
konieczności rekompilacji programu.

%description -l pt_BR.UTF-8
O libglade permite carregar, em tempo de execução, arquivos da
interface glade. Não é necessário ter o glade instalado, mas esta é a
melhor maneira de criar os arquivos de interface.

%package devel
Summary:	Header files and developer's documentation
Summary(es.UTF-8):	Archivos necesarios para el desarrollo de aplicaciones con libglade
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja dla programisty
Summary(pt_BR.UTF-8):	Arquivos necessários para o desenvolvimento de aplicações com a interface glade
Group:		X11/Development/Libraries
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtk+2-devel >= 2:2.10.13
Requires:	libxml2-devel >= 1:2.6.29
Obsoletes:	libglade2.0-devel

%description devel
Header files and developer's documentation for libglade.

%description devel -l es.UTF-8
Archivos de inclusión y bibliotecas necesarias para el desarrollo de
aplicaciones con glade.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja dla programisty libglade.

%description devel -l pt_BR.UTF-8
Arquivos de inclusão e bibliotecas para o desenvolvimento de
aplicações com a interface glade.

%package static
Summary:	Static libglade library
Summary(es.UTF-8):	Archivos estáticos necesarios para el desarrollo de aplicaciones con libglade
Summary(pl.UTF-8):	Biblioteka statyczna libglade
Summary(pt_BR.UTF-8):	Arquivos estáticos necessários para o desenvolvimento de aplicações com a interface glade
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description static
Static libglade library.

%description static -l es.UTF-8
Archivos estáticos necesarias para el desarrollo de aplicaciones con
glade.

%description static -l pl.UTF-8
Biblioteka statyczna libglade.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para o desenvolvimento de aplicações com a
interface glade.

%package apidocs
Summary:	libglade API documentation
Summary(pl.UTF-8):	Dokumentacja API libglade
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libglade API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API libglade.

%prep
%setup -q -n libglade-%{version}

%build
%{?with_apidocs:%{__gtkdocize}}
%{__libtoolize}
%{__glib_gettextize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--%{?with_apidocs:en}%{!?with_apidocs:dis}able-gtk-doc \
	--with-html-path=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/libglade/2.0

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	HTML_DIR=%{_gtkdocdir} \
	pkgconfigdir=%{_pkgconfigdir}

%{!?with_apidocs:rm -rf $RPM_BUILD_ROOT%{_gtkdocdir}}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/libglade-2.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libglade-2.0.so.0
%{_libdir}/libglade
%dir %{_datadir}/xml/libglade
%{_datadir}/xml/libglade/*.dtd

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_bindir}/libglade-convert
%attr(755,root,root) %{_libdir}/libglade-2.0.so
%{_pkgconfigdir}/*
%{_includedir}/libglade-2.0

%files static
%defattr(644,root,root,755)
%{_libdir}/libglade-2.0.a

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libglade
%endif
