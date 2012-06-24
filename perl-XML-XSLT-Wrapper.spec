#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	XML
%define	pnam	XSLT-Wrapper
Summary:	XML::XSLT::Wrapper - Consistent interface to XSLT processors
Summary(pl):	XML::XSLT::Wrapper - sp�jny interfejs do procesor�w XSLT
Name:		perl-XML-XSLT-Wrapper
Version:	0.32
Release:	0.2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MU/MULL/XML-XSLT-Wrapper-%{version}.tar.gz
# Source0-md5:	d08350e5d6a45d5e42ac7ab5fa80fd45
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# found from inline code
%define		_noautoreq	'perl(XML::Xalan::Transformer)'

%description
Provides a consistent interface to various XSLT processors. Tries each
of a supplied list of processors in turn until one performs a
successful transform. If no list is given, tries all the processors it
knows until one works. Does its best to fail gracefully whenever a
processor does not work for some reason.

%description -l pl
Ten modu� udost�pnia sp�jny interfejs do r�nych procesor�w XSLT.
Pr�buje ka�dy z dostarczonej listy procesor�w a� kt�rych wykona
pomy�lnie przekszta�cenie. Je�li nie przekazano listy procesor�w,
pr�buje wszystkich znanych sobie procesor�w. Usi�uje zachowa� si� jak
najlepiej w przypadku niepowodzenia kt�rego� z procesor�w.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README TODO
%dir %{perl_vendorlib}/XML/XSLT
%{perl_vendorlib}/XML/XSLT/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
