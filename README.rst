===========
ConfigCollector
===========
This tool collects configuration file of multiple routers.

Support router OS
==============
* IOS
* IOS-XE
* IOS-XR
* JUNOS

Install
=====
Install using pip
::
    pip install configcolletctor

How to use
==============
Use following format
::
    python configcollector.py -i [inventory_file] -o [output_dirctory]

* inventory_file
    Router infomation file using Json format.
    The router OS is select from the below list. ::
        * JUNOS
        * IOS
        * IOS-XE
        * IOS-XR

    Exmaple
    ::
        [
            {
                "hostname" : "router1",
                "username" : "user1",
                "password" : "aaabbbccc",
                "ipv4"     : "192.168.0.1",
                "os"       : "JUNOS"
            },
            {
                "hostname" : "router2",
                "username" : "user2",
                "password" : "aaabbbccc",
                "ipv4"     : "192.168.0.2",
                "os"       : "IOS-XR"
            },
            {
                "hostname" : "router3",
                "username" : "user3",
                "password" : "aaabbbccc",
                "ipv4"     : "192.168.0.3",
                "os"       : "IOS"
            }
        ]

* output_directory
    The directory placed router configuration output files by ConfigCollector.
 
    Defalt : Current directory
