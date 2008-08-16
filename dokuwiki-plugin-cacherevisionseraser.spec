%define		plugin		cacherevisionseraser
Summary:	DokuWiki cacherevisionseraser plugin
Summary(pl.UTF-8):	Wtyczka cacherevisionseraser dla DokuWiki
Name:		dokuwiki-plugin-%{plugin}
Version:	1.6.1
Release:	0.1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://ph0x.drunkencoders.com/dokuwikiplugin/dokuwiki_plugin_cacherevisions_eraser.zip
# Source0-md5:	16a5ecef695bc41b07d3ae397f0098ea
Source1:	dokuwiki-find-lang.sh
URL:		http://wiki.splitbrain.org/plugin:cacherevisionseraser
Requires:	dokuwiki >= 20061106
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_dokudir	/usr/share/dokuwiki
%define		_plugindir	%{_dokudir}/lib/plugins/%{plugin}

%description
This admin plug-in allows you to erase the entire cache and/or old
wiki revisions. Only use this plug-in if you want to clean up your
wiki or if the cache gets corrupted.

%description -l pl.UTF-8
Wtyczka do usuwania cache-u i/oraz starych rewizii wiki.

%prep
%setup -q -n cacherevisionserase

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_plugindir}
cp -a . $RPM_BUILD_ROOT%{_plugindir}

# find locales
sh %{SOURCE1} %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc readme.txt readme_unix.txt
%dir %{_plugindir}
%{_plugindir}/*.php
