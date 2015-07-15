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
Install using pip.
::
    pip install configcolletctor

How to use
==============
Use following format.
::
    configcollector -i [inventory_file] -o [output_dirctory]

* inventory_file
    Router infomation file using Json format.
    The router OS is select from the below list. ::
        * JUNOS
        * IOS
        * IOS-XE
        * IOS-XR

    Sample inventory file
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

Example
=======
Example to get router config files using ConfigCollector.
::
    % mkdir router_config

    % python configcollector.py -i sample_routers.json -o router_config/
    
    Accessing router: router1...
    Writing output file "router_config/router1"...
    Success : "router_config/router1"!
    Accessing router: router2...
    Writing output file "router_config/router2"...
    Success : "router_config/router2"!
    Accessing router: router3...
    Writing output file "router_config/router3"...
    Success : "router_config/router3"!
    
    % ls routera_config
    router1.txt  router2.txt  router3.txt
    
    % less router1.txt
    
    show configuration | no-more
    ## Last commit: 2015-05-01 17:00:00 JST by user1
    version x.x.x;
    system {
        host-name router1;
        time-zone Asia/Tokyo;
    (snip)

    
    
