# GitRouter
Router configuration management tool using git.

# Support router OSs
- JUNOS
- IOS-XR
- IOS
- IOS-XE

## How to use

```
python example.txt sample.json
```

You can describe multipul routers using json format.

```sample.json
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

The router configuration is saved in "router_config" directory.

```
$ ls router_config 
router1.txt  router2.txt router3.txt
```

```
$ less router1.txt

show configuration | no-more
## Last commit: 2015-05-01 17:00:00 JST by user1
version 10.x.x;
system {
    host-name router1;
    time-zone Asia/Tokyo;
(snip)
```


