Summary:	tail program using kernel DNOTIFY-api
Summary(pl.UTF-8):	Program tail używający API jądra DNOTIFY
Name:		turbotail
Version:	0.3
Release:	1
License:	GNU
Group:		Applications/Text
Source0:	http://www.vanheusden.com/turbotail/%{name}-%{version}.tgz
# Source0-md5:	a4eecdd0cae9552f17cb1c540a08f6f2
URL:		http://www.vanheusden.com/Linux/#logging
BuildRequires:	fam-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A drop-in replacement for the original (GNU-)tail program which uses
the (Linux-)kernel DNOTIFY-api instead of polling every second(!).

%description -l pl.UTF-8
Zamiennik oryginalnego programu (GNU-)tail używający API jądra
(Linuksa) DNOTIFY zamiast sprawdzania co sekundę.

%prep
%setup -q

%build
%{__make} \
	DEBUG="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt
%attr(755,root,root) %{_bindir}/*
