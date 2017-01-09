===========
ConfigCollector
===========
This tool collects configuration file of multiple routers.

Support router OS
==============
* IOS
* IOS-XE
* IOS-XR
* NX-OS
* ASA
* JUNOS

Install
=====
Install using pip.
::
    pip install configcollector

How to use
==============
Use following format.
::
    configcollector -i [inventory_file] -o [output_directory]

* inventory_file
    Router infomation file using Json format.
    The router OS is select from the below list. ::
        * IOS
        * IOS-XE
        * IOS-XR
        * NX-OS
        * ASA
        * JUNOS

    Defalt : /etc/configcollector/inventory.json

    Sample inventory file
    ::
        [
          {
              "hostname" : "IOS-Sample",
              "username" : "USER",
              "password" : "PASSWORD",
              "ipv4"     : "192.168.0.1",
              "os"       : "IOS"
          },
          {
              "hostname" : "ASA-Sample",
              "username" : "USER",
              "password" : "PASSWORD",
              "enable"   : "ENABLE",
              "ipv4"     : "192.168.0.5",
              "os"       : "ASA"
          },
          {
              "hostname" : "JUNOS-Sample",
              "username" : "USER",
              "password" : "PASSWORD",
              "ipv4"     : "192.168.0.6",
              "os"       : "JUNOS"
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

    % configcollector -i sample_routers.json -o router_config/

    Accessing router: router1...
    Writing output file "router_config/router1"...
    Success : "router_config/router1"!
    Accessing router: router2...
    Writing output file "router_config/router2"...
    Success : "router_config/router2"!
    Accessing router: router3...
    Writing output file "router_config/router3"...
    Success : "router_config/router3"!

    % ls router_config
    router1.txt  router2.txt  router3.txt

    % less router1.txt

    show configuration | no-more
    ## Last commit: 2015-05-01 17:00:00 JST by user1
    version x.x.x;
    system {
        host-name router1;
        time-zone Asia/Tokyo;
    (snip)
