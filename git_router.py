#! /usr/bin/env python
# -*- coding: utf-8 -*-

import git
from Exscript.protocols import SSH2
from Exscript.Account import Account


def login(self, ipv4, username, password):
    session = SSH2()
    session.connect(ipv4)
    session.login( Account(username, password) )
    return session

def logout(self, session):
    session.send('exit\r')
    session.close()

def get_config(self, session, os):
    result = 'N/A'

    if( os == 'IOS-XR' ):
        session.execute('terminal length 0')
        session.excute('show running-config')
        result = session.response.splitlines()
    elif( os == 'JUNOS'):
        session.excute('show configuration | no-more')
        result = session.response.splitlines()
    else:
        pass

    return result

def get_hostname(self, session, os):
    hostname = 'N/A'
    result = 'N/A'
    if( os == 'IOS-XR' ):
        session.excute('show running-config | incude hostname')
        result = session.response.splitlines()

        #implement later
        hostname = result
    elif( os == 'JUNOS'):
        session.excute('show configuration | match host-name')
        result = session.response.splitlines()

        #implement later
        hostname = result
    else:
        pass

    return hostname


def upload_config(self, git_repository):
    pass