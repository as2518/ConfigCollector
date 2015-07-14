#! /usr/bin/env python
# -*- coding: utf-8 -*-

from Exscript.protocols import SSH2
from Exscript.Account import Account


class Router:
    def __init__(self, router_info):
        self.hostname = router_info['hostname']
        self.username = router_info['username']
        self.password = router_info['password']
        self.ipv4 = router_info['ipv4']
        self.os = router_info['os']

    def login(self):
        self.session = SSH2()
        self.session.connect(self.ipv4)
        self.session.login(Account(name=self.username, password=self.password))

    def logout(self):
        if self.session:
            self.session.send('exit\r')
            self.session.close()
        else:
            raise AttributeError('cannot find a living session.')

    def get_config(self):
        if(self.os == 'IOS-XR' or self.os == 'IOS' or self.os == 'IOS-XE'):
            self.session.execute('terminal length 0')
            self.session.execute('show running-config')
            result = self.session.response
        elif(self.os == 'JUNOS'):
            self.session.execute('show configuration | no-more')
            result = self.session.response
        else:
            raise ValueError('OS is unknown value.\
                Please describe from  JUNOS / IOS / IOS-XE / IOS-XR.')
        return result
