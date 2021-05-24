#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-HTTP-Server-Simple
Version  : 0.52
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/B/BP/BPS/HTTP-Server-Simple-0.52.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BP/BPS/HTTP-Server-Simple-0.52.tar.gz
Summary  : 'Lightweight HTTP server'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-HTTP-Server-Simple-perl = %{version}-%{release}
Requires: perl(CGI)
BuildRequires : buildreq-cpan
BuildRequires : perl(CGI)

%description
HTTP::Server::Simple is a very simple standalone HTTP daemon with no non-core
module dependencies.  It's ideal for building a standalone http-based UI to
your existing tools.

%package dev
Summary: dev components for the perl-HTTP-Server-Simple package.
Group: Development
Provides: perl-HTTP-Server-Simple-devel = %{version}-%{release}
Requires: perl-HTTP-Server-Simple = %{version}-%{release}

%description dev
dev components for the perl-HTTP-Server-Simple package.


%package perl
Summary: perl components for the perl-HTTP-Server-Simple package.
Group: Default
Requires: perl-HTTP-Server-Simple = %{version}-%{release}

%description perl
perl components for the perl-HTTP-Server-Simple package.


%prep
%setup -q -n HTTP-Server-Simple-0.52
cd %{_builddir}/HTTP-Server-Simple-0.52

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/HTTP::Server::Simple.3
/usr/share/man/man3/HTTP::Server::Simple::CGI.3
/usr/share/man/man3/HTTP::Server::Simple::CGI::Environment.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/HTTP/Server/Simple.pm
/usr/lib/perl5/vendor_perl/5.34.0/HTTP/Server/Simple/CGI.pm
/usr/lib/perl5/vendor_perl/5.34.0/HTTP/Server/Simple/CGI/Environment.pm
