#!/bin/bash -x

rm -rfv server-1 server-2
key=$(tsig-keygen)
cp -r 1 server-1
echo $key >>server-1/named.conf.local 
cp -r 2 server-2
echo $key >>server-2/named.conf.local 

