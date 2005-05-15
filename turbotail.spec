Summary:	tail program using kernel DNOTIFY-api
Summary(pl):	Program tail u¿ywaj±cy API j±dra DNOTIFY
Name:		turbotail
Version:	0.2
Release:	0.1
Epoch:		0
License:	GNU
Group:		Applications/Text
Source0:	http://www.vanheusden.com/Linux/%{name}-%{version}.tgz
# Source0-md5:	24903c65622391e62f238218cfc5c2d7
URL:		http://www.vanheusden.com/Linux/#logging
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A drop-in replacement for the original (GNU-)tail program which uses
the (Linux-)kernel DNOTIFY-api instead of polling every second(!).

%description -l pl
Zamiennik oryginalnego programu (GNU-)tail u¿ywaj±cy API j±dra
(Linuksa) DNOTIFY zamiast sprawdzania co sekundê.

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
