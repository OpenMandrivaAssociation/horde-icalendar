%define prj    iCalendar

%define xmldir  %{_var}/lib/pear
%define peardir %(pear config-get php_dir 2> /dev/null)

Name:          horde-icalendar
Version:       0.1.0
Release:       %mkrel 4
Summary:       The horde iCalendar API
License:       LGPL
Group:         Networking/Mail
Url:           http://pear.horde.org/index.php?package=%{prj}
Source0:       %{prj}-%{version}.tgz
BuildArch:     noarch
Requires(post):php-pear
Requires(preun):php-pear
Requires(pre): php-pear
Requires:      horde-util
Requires:      php-pear
BuildRequires: dos2unix
BuildRequires: php-pear
BuildRequires: php-pear-channel-horde


%description
This package provides an API for dealing with iCalendar data.


%prep
%setup -q -n %{prj}-%{version}

%build
%__mv ../package.xml .

%install
pear -d doc_dir=%{_docdir}/horde install --packagingroot %{buildroot} --nodeps package.xml
dos2unix %{buildroot}%{_docdir}/horde/iCalendar/docs/examples/exdate.ics
dos2unix %{buildroot}%{_docdir}/horde/iCalendar/docs/examples/vnote.txt

%__rm -rf %{buildroot}/%{peardir}/.{filemap,lock,registry,channels,depdb,depdblock}

%__mkdir_p %{buildroot}%{xmldir}
%__cp package.xml %{buildroot}%{xmldir}/%{prj}.xml

%clean
%__rm -rf %{buildroot}

%post
pear install --nodeps --soft --force --register-only %{xmldir}/%{prj}.xml

%postun
if [ "$1" -eq "0" ]; then
  pear uninstall --nodeps --ignore-errors --register-only pear.horde.org/%{prj}
fi

%files
%defattr(-, root, root)
%{xmldir}/%{prj}.xml
%dir %{peardir}/Horde/iCalendar
%{peardir}/Horde/iCalendar.php
%{peardir}/Horde/iCalendar/valarm.php
%{peardir}/Horde/iCalendar/vcard.php
%{peardir}/Horde/iCalendar/vevent.php
%{peardir}/Horde/iCalendar/vfreebusy.php
%{peardir}/Horde/iCalendar/vjournal.php
%{peardir}/Horde/iCalendar/vnote.php
%{peardir}/Horde/iCalendar/vtimezone.php
%{peardir}/Horde/iCalendar/vtodo.php
%dir %{_docdir}/horde/iCalendar
%dir %{_docdir}/horde/iCalendar/docs
%dir %{_docdir}/horde/iCalendar/docs/examples
%{_docdir}/horde/iCalendar/docs/examples/exchange.ics
%{_docdir}/horde/iCalendar/docs/examples/exdate.ics
%{_docdir}/horde/iCalendar/docs/examples/parser.php
%{_docdir}/horde/iCalendar/docs/examples/vnote.txt
%dir %{peardir}/tests/iCalendar
%dir %{peardir}/tests/iCalendar/tests
%{peardir}/tests/iCalendar/tests/charset1.phpt                                                                                    
%{peardir}/tests/iCalendar/tests/iCalendar.phpt                                                                                    
%{peardir}/tests/iCalendar/tests/read-escapes.phpt                                                                                 
%{peardir}/tests/iCalendar/tests/read-vcard-org.phpt                                                                               
%{peardir}/tests/iCalendar/tests/read-write-escapes.phpt                                                                           
%{peardir}/tests/iCalendar/tests/timezones.phpt                                                                                    
%{peardir}/tests/iCalendar/tests/vfreebusy.phpt                                                                                    
%{peardir}/tests/iCalendar/tests/write-escapes.phpt

