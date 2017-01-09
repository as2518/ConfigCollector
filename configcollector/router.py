# -*- coding: utf-8 -*-
"""Definition Router."""
from Exscript.protocols import SSH2
from Exscript.Account import Account


class Router:

    """Router class."""

    def __init__(self, router_info):
        """Initialize."""
        self.hostname = router_info['hostname']
        self.username = router_info['username']
        self.password = router_info['password']
        if router_info.has_key('enable'):
            self.enable = router_info['enable']
        else:
            self.enable = None
        self.ipv4 = router_info['ipv4']
        self.os_name = router_info['os']
        self.session = None

    def login(self):
        """login."""
        self.session = SSH2()
        self.session.connect(self.ipv4)
        self.session.login(Account(name=self.username, password=self.password))

    def logout(self):
        """logout."""
        if self.session:
            self.session.send('exit\r')
            self.session.close()
        else:
            raise AttributeError('cannot find a living session.')

    def get_config(self):
        """get configuration."""
        if (
                self.os_name == 'IOS' or
                self.os_name == 'IOS-XE' or
                self.os_name == 'IOS-XR' or
                self.os_name == 'NX-OS'):
            if not self.enable is None:
                self.session.send('enable\r')
                self.session.execute(self.enable)
            self.session.execute('terminal length 0')
            self.session.execute('show running-config')
            result = self.session.response
        elif self.os_name == 'ASA':
            # see below:
            # https://groups.google.com/forum/#!topic/exscript/bWzhSb__g64
            self.session.send('enable\r')
            self.session.execute(self.enable)
            self.session.execute('terminal pager 0')
            self.session.execute('show running-config')
            result = self.session.response
        elif self.os_name == 'JUNOS':
            if self.username == 'root':
                self.session.execute('cli show configuration | no-more')
            else:
                self.session.execute('show configuration | no-more')
            result = self.session.response
        else:
            raise ValueError('OS is unknown value.\
                Please describe from IOS / IOS-XE / IOS-XR / NX-OS / ASA / JUNOS.')
        return result
