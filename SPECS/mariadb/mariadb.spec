Summary:        Database servers made by the original developers of MySQL.
Name:           mariadb
Version:        10.1.24
Release:        1%{?dist}
License:        GPLv2
Group:          Applications/Databases
Vendor:         VMware, Inc.
Distribution:   Photon
Url:            https://mariadb.org/
Source0:        http://mirrors.syringanetworks.net/mariadb/mariadb-%{version}/source/mariadb-%{version}.tar.gz
%define         sha1 mariadb=77bf12f253bc4397fa0379dcdba81ae8f6f03d17

BuildRequires:  cmake
BuildRequires:  Linux-PAM-devel
BuildRequires:  openssl-devel
BuildRequires:  zlib-devel

%description
MariaDB Server is one of the most popular database servers in the world. It’s made by the original developers of MySQL and guaranteed to stay open source. Notable users include Wikipedia, WordPress.com and Google.

MariaDB turns data into structured information in a wide array of applications, ranging from banking to websites. It is an enhanced, drop-in replacement for MySQL. MariaDB is used because it is fast, scalable and robust, with a rich ecosystem of storage engines, plugins and many other tools make it very versatile for a wide variety of use cases.

%package devel
Summary:        Development headers for mariadb
Requires:       %{name} = %{version}-%{release}

%description devel
Development headers for developing applications linking to maridb


%prep
%setup -q %{name}-%{version}

%build
cmake . \
      -DCMAKE_INSTALL_PREFIX=/usr   \
      -DCMAKE_BUILD_TYPE=Release    \
      -DINSTALL_MANDIR=share/man \
      -DINSTALL_DOCDIR=share/doc \
      -DINSTALL_DOCREADMEDIR=share/doc/%{name} \
      -DINSTALL_SUPPORTFILESDIR=share/support-files \
      -DINSTALL_SYSCONFDIR="%{_sysconfdir}" \
      -Wno-dev

make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install

%check
make check

%files
%defattr(-,root,root)
%{_libdir}/plugin/*
%{_libdir}/libmysqlclient.so.*
%{_libdir}/libmysqlclient_r.so.*
%{_bindir}/*
%{_mandir}/man1/*
%{_mandir}/man8/*
/usr/scripts/mysql_install_db
%config(noreplace) %{_sysconfdir}/logrotate.d/mysql
%config(noreplace) %{_sysconfdir}/my.cnf
%{_datadir}/charsets/*
%{_datadir}/support-files/*
%{_datadir}/czech/errmsg.sys
%{_datadir}/danish/errmsg.sys
%{_datadir}/dutch/errmsg.sys
%{_datadir}/english/errmsg.sys
%{_datadir}/errmsg-utf8.txt
%{_datadir}/estonian/errmsg.sys
%{_datadir}/fill_help_tables.sql
%{_datadir}/french/errmsg.sys
%{_datadir}/german/errmsg.sys
%{_datadir}/greek/errmsg.sys
%{_datadir}/hungarian/errmsg.sys
%{_datadir}/install_spider.sql
%{_datadir}/italian/errmsg.sys
%{_datadir}/japanese/errmsg.sys
%{_datadir}/korean/errmsg.sys
%{_datadir}/maria_add_gis_sp.sql
%{_datadir}/maria_add_gis_sp_bootstrap.sql
%{_datadir}/mroonga/install.sql
%{_datadir}/mroonga/uninstall.sql
%{_datadir}/mysql_performance_tables.sql
%{_datadir}/mysql_system_tables.sql
%{_datadir}/mysql_system_tables_data.sql
%{_datadir}/mysql_test_data_timezone.sql
%{_datadir}/mysql_to_mariadb.sql
%{_datadir}/norwegian-ny/errmsg.sys
%{_datadir}/norwegian/errmsg.sys
%{_datadir}/pkgconfig/mariadb.pc
%{_datadir}/polish/errmsg.sys
%{_datadir}/portuguese/errmsg.sys
%{_datadir}/romanian/errmsg.sys
%{_datadir}/russian/errmsg.sys
%{_datadir}/serbian/errmsg.sys
%{_datadir}/slovak/errmsg.sys
%{_datadir}/spanish/errmsg.sys
%{_datadir}/swedish/errmsg.sys
%{_datadir}/ukrainian/errmsg.sys
%doc COPYING CREDITS README

%exclude %{_sysconfdir}/init.d/*
%exclude /usr/sql-bench
%exclude /usr/mysql-test
%exclude /usr/data/test/*
%exclude /usr/share/doc

%files devel
%{_libdir}/libmysqlclient.so
%{_libdir}/libmysqlclient_r.so
%{_libdir}/*.a
%{_includedir}/mysql/*
%{_datadir}/aclocal/mysql.m4

%changelog
*   Wed Apr 05 2017 Xiaolin Li <xiaolinl@vmware.com> 10.1.24-1
-   Initial packaging for Photon
