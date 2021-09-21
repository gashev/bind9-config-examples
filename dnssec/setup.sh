#!/bin/bash

rm -rfv server-1
mkdir server-1
cd server-1
mkdir conf
cp -r ../conf/server-1/* conf/
mkdir cache
chown -R 105.106 cache
cd conf
dnssec-keygen -a NSEC3RSASHA1 -b 2048 -n ZONE test.devel
dnssec-keygen -f KSK -a NSEC3RSASHA1 -b 4096 -n ZONE test.devel

for key in $(ls Ktest.devel*.key)
do
	echo "\$INCLUDE $key">> db.test.devel
done

dnssec-signzone -A -3 $(head -c 1000 /dev/random | sha1sum | cut -b 1-16) -N INCREMENT -o test.devel -t db.test.devel
