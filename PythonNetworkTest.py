# This will conduct basic network troubleshooting on local computer
# 1 is an ICMP ping, loopback, then 3 public facing IPs from popular DNS providers
# 2 is a DNS resolution test with an ICMP ping to resolve DNS domain names
# 3 is a tracert to 3 public facing popular DNS providers
# 4 is a WLAN report for SSIDs and things like signal strength and more
# 5 is an ARP scan for neighbor discovery

# Dependencies
# pip install scapy

# Imports
from __future__ import print_function
from cProfile import run
from subprocess import Popen, PIPE
from pickle import TRUE
from telnetlib import IP, theNULL
import os
import scapy.all as scapy
import subprocess
import socket

######################################Functions######################################
def get_privateIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    print(s.getsockname()[0])
    s.close()

def ip_test():
    ip_hosts = ['127.0.0.1', '8.8.8.8', '9.9.9.9', '1.1.1.1'] # list of public IP addresses to test connectivity with ICMP ping, tests loopback address and then some public IPs
    for ip_host in ip_hosts:
        os.system('ping ' + ip_host)

def dns_test():
    dns_hosts = ['google.com', 'quad9.net', 'cloudflare.com'] # list of DNS names to resolve, to test DNS resolution with ICMP ping
    for dns_host in dns_hosts:
        os.system('ping ' + dns_host)

def tracer():
    trace_hosts = ['8.8.8.8', '9.9.9.9', '1.1.1.1'] # list of IP addresses to test connectivity with ICMP ping, conducts tracert to see hops
    for trace_host in trace_hosts:
        p = Popen(['tracert', trace_host], stdout=PIPE)
        while True:
            try:
                line = p.stdout.readline()
                if not line:
                    break
                print (line.rstrip())
            except:
                break

def wlan_report():
    ssid_stats = subprocess.run (['netsh', 'wlan', 'show', 'all'],
                            capture_output=True, text=True)
    print(ssid_stats.stdout)

class scan:
    def arp_request(self, ip):
        self.ip = ip
        print(ip)
        arp_r = scapy.ARP(pdst=ip)
        br = scapy.Ether(dst='ff:ff:ff:ff:ff:ff')
        request = br/arp_r
        answered, unanswered = scapy.srp(request, timeout=1)
        print('\tIP\t\t\t\t\tMAC')
        print('_' * 37)
        for i in answered:
            ip, mac = i[1].psrc, i[1].hwsrc
            print(ip, '\t\t' + mac)
            print('-' * 37)

def arp_scan():
    arp = scan() # creates instance
    arp.arp_request(get_privateIP()) # call the class

def switch_calls():
   while True:
    user_input = int(input('1 for Ping, 2 for DNS Resolution, 3 for Tracert, 4 for WLAN report, 5 for ARP, 0 to Exit : '))

    if user_input == 1:
       ip_test()

    elif user_input == 2:
       dns_test()

    elif user_input == 3:
        tracer()
    
    elif user_input == 4:
        wlan_report()

    elif user_input == 5:
        arp_scan()

    else:
       print('Please make another selection or press 0 to exit')
       if user_input == 0:
        exit()

######################################End of Functions######################################

switch_calls()
