#! /usr/bin/env python
import sys

from git_router import Router
from json import loads

file_input = open(sys.argv[1] ,'r')
router_info_json = file_input.read()
file_input.close()

print 'Read ' + sys.argv[1] + '!'

router_info = loads(router_info_json) 

for num in range( len(router_info) ):
    router = Router( router_info[num] )

    router.login()
    router_config = router.get_config()
    router.logout()

    filename = 'error'
    filename = 'router_config/' + router_info[num]['hostname'] + '.txt'
    file_output = open ( filename, 'w')
    file_output.write( router_config ) 
    file_output.close

    print 'Created ' + filename +' !'

    #router.gitpush_config( router_config )

