class httpd {
yumrepo {"repo163":
 descr => "163",
 baseurl => "http://mirrors.163.com/centos/5/os/x86_64/",
 gpgcheck => "0",
 enabled => "1",
}

 package { 
 "httpd":
 ensure => installed, 
 require => Yumrepo["repo163"],
} 
} 
