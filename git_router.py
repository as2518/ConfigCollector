#! /usr/bin/env python
# -*- coding: utf-8 -*-

from git import Repo
from Exscript.protocols import SSH2
from Exscript.Account import Account

class Router:
    def __init__(self, ipv4, username, password, os):
        self.ipv4 = ipv4
        self.username = username
        self.password = password
        self.os = os

    def login(self):
        self.session = SSH2()
        self.session.connect(self.ipv4)
        self.session.login( Account(self.username, self.password) )
        return self.session

    def logout(self):
        self.session.send('exit\r')
        self.session.close()

    def get_config(self):
        result = 'N/A'

        if( self.os == 'IOS-XR' ):
            self.session.execute('terminal length 0')
            self.session.excute('show running-config')
            result = self.session.response.splitlines()
        elif( self.os == 'JUNOS'):
            self.session.excute('show configuration | no-more')
            result = self.session.response.splitlines()
        else:
            pass

        return result

    def get_hostname(self):
        hostname = 'N/A'
        result = 'N/A'
        if( self.os == 'IOS-XR' ):
            self.session.excute('show running-config | incude hostname')
            result = self.session.response.splitlines()

            #implement later
            hostname = result
        elif( self.os == 'JUNOS'):
            self.session.excute('show configuration | match host-name')
            result = self.session.response.splitlines()

            #implement later
            hostname = result
        else:
            pass

        return hostname


    def upload_config(self, config_file):
        pass