#!/usr/bin/env python

# from IPy import IP
#
# ip_s = raw_input('Please input an IP or net-range: ')
# ips = IP(ip_s)
# if len(ips) > 1:
#     print 'net: %s' % ips.net()
#     print 'netmask: %s' % ips.netmask()
#     print 'broadcast: %s' % ips.broadcast()
#     print 'reverse address: %s' % ips.reverseNames()[0]
#     print 'subnet: %s' % len(ips)
# else:
#     print 'reverse address: %s' % ips.reverseNames()[0]
#
# print 'hexadecimal: %s' % ips.strHex()
# print 'binary ip: %s' % ips.strBin()
# print 'iptype: %s' % ips.iptype()


import dns.resolver

# domain = raw_input('Please inpu an domain: ')
# A = dns.resolver.query(domain,'A')
# for i in A.response.answer:
#     for j in i.items:
#         print j.address
# domain = raw_input('Please input an domain: ')
# MX = dns.resolver.query(domain,'MX')
# for i in MX:
#     print 'MX preference = ',i.preference,'mail exchanger =',i.exchange

domain = raw_input('Please input an domain: ')
ns = dns.resolver.query(domain,'NS')
for i in ns.response.answer:
    for j in i.items:
        print j.to_text()