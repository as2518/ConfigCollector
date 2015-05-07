#! /usr/bin/env python
import sys
import traceback
import json

from execute_router import Router

try:
    # argument is routers' information with JSON formt.
    input_filename = sys.argv[1]
    input_file = open(input_filename ,'r')
    print 'Reading router info from "' + input_filename + '"...' 
except ( IOError, IndexError):
    print 'Cannot open JSON file.'
    print 'Please use bellow: " python get_router_config [JSON file] " '
    sys.exit()
else:
    router_info_json = input_file.read()
    input_file.close()

try:
    router_info = json.loads(router_info_json)
except ValueError as error:
    print 'JSON format error : '
    print router_info_json
    print error
    sys.exit()

for num in range( len(router_info) ):
    router = Router( router_info[num] )
    print 'Accessing router: ' + router_info[num]['hostname'] + '...'
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
        output_filename = 'router_config/' + router_info[num]['hostname'] + '.txt'
        print 'Writing output file "' + output_filename + '"...'
    except AtributeError:
        print 'cannot read dictionary of router_info[' + num + '][hostname]'
        sys.exit()

    try:
        output_file = open ( output_filename, 'w')
    except:
        print 'cannot open "' + output_filename + '"'
        output_file.close
        sys.exit()
    else:
        output_file.write( router_config )
        output_file.close

    print 'Success to create "'  + output_filename + '" !'
