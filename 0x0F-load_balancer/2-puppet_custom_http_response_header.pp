#!/usr/bin/env bash
# Using puppet to add custom HTTPS
add_header {"/etc/ngnix/nginx.conf":
	owner   => 'www-data'
	group   => 'www-data'
	content => 'X-Served-By $hostname'
	source  => "puppet://etc/nginx/nginx.conf"
}
