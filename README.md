# GetRouterConfig
Router configuration management tool.

# Support router's OSs
- JUNOS
- IOS-XR
- IOS
- IOS-XE

# Install
Download this tool.

```
$ git clone git@github.com:taijiji/GetRouterConfig.git
```

Install python module using pip.

```
$ pip install -r requirements.txt
```

# How to use this tool

```
python get_router_config.py [json file]
```

You can describe multipul routers using json format.
The router's OS is select from the below list.
- JUNOS
- IOS
- IOS-XE
- IOS-XR

This is sample json file.

```my_router.json
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
    },
]
```

After running this tool, the gotten router configuration is saved under "router_config" directory.

Example:

```
$ ls router_config
router1.txt  router2.txt  router3.txt
```

```
$ less  router_config/router1.txt

show configuration | no-more
## Last commit: 2015-05-01 17:00:00 JST by user1
version 10.x.x;
system {
    host-name router1;
    time-zone Asia/Tokyo;
(snip)
```

# blog
Posted technical blog in Qiita (In Japanese).
http://qiita.com/taijijiji/items/620908c1bec27e1ea933
