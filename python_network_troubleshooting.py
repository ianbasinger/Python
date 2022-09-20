# Dependencies : pip install traceroute

from subprocess import Popen, PIPE
import sys
from operator import truediv
import os
from pickle import TRUE
from telnetlib import theNULL

def ip_test():
    ip_hosts = ['127.0.0.1', '8.8.8.8', '9.9.9.9', '1.1.1.1'] # list of public IP addresses to test connectivity with ICMP ping, tests loopback address and then some public IPs
    for ip_host in ip_hosts:
        os.system('ping ' + ip_host)

def dns_test():
    dns_hosts = ['google.com', 'quad9.net', 'cloudflare.com'] # list of DNS names to resolve, to test DNS resolution with ICMP ping
    for dns_host in dns_hosts:
        os.system('ping ' + dns_host)

def tracer():
    hosts = ['8.8.8.8', '9.9.9.9', '1.1.1.1'] # list of IP addresses to test connectivity with ICMP ping, conducts tracert to see hops
    for host in hosts:
        p = Popen(['tracert', host], stdout=PIPE)
        while True:
            try:
                line = p.stdout.readline()
                if not line:
                    break
                print (line.rstrip())
            except:
                break

ip_test()
dns_test()
tracer()