#! /usr/bin/env python
import sys
import traceback
import json

from ssh_router import Router

try:
    # argument is routers' information with JSON formt.
    file_input = open(sys.argv[1] ,'r')
except ( IOError, IndexError):
    print 'Cannot open JSON file.'
    print 'Please use bellow: " python get_router_config [JSON file] " '
    sys.exit()
else:
    router_info_json = file_input.read()
    file_input.close()

try:
    router_info = json.loads(router_info_json)
except ValueError as error:
    print 'JSON format error : '
    print router_info_json
    print error
    sys.exit()

for num in range( len(router_info) ):
    router = Router( router_info[num] )

    try:
        router.login()
        router_config = router.get_config()
    except:
        print 'Router login error'
        print router_info[num]
        router.logout()
        sys.exit()

    try:
        router_config = router.get_config()
    except:
        print 'Router get configuration error'
        print router_info[num]
        router.logout()
        sys.exit()
    else:
        router.logout()

    try:
        filename = 'router_config/' + router_info[num]['hostname'] + '.txt'
    except AtributeError:
        print 'cannot read dictionary of router_info[' + num + '][hostname]'
        sys.exit()

    try:
        file_output = open ( filename, 'w')
        file_output.write( router_config )
    except:
        print 'cannot open ' + filename
        file_output.close
        sys.exit()
    else:
        file_output.close

    print 'Success to create "'  + filename +'" !'
