#! /usr/bin/env python
import sys
from argparse import ArgumentParser
from file_handler import readfile, writefile, convert_jason_to_dict
from ssh_router import Router

parser = ArgumentParser(description='Collect configuration files on mutiple routers')
parser.add_argument(    '-i', '--inventory',
                            type=str,
                            default='/etc/configcollector/inventory',
                            help='router information file\n(default=/etc/configcollector/inventory)')
parser.add_argument(   '-o',  '--output',
                            type=str,
                            default='./',
                            help='output directory\n(default=CURRENT_DIRECTORY/router_config/)' )
args = parser.parse_args()


router_info = convert_jason_to_dict( readfile( args.inventory ) )

# Login and get config each routers using ssh
for num in range( len(router_info) ):
    router = Router( router_info[num] )

    # Login and get config of Router
    print 'Accessing router: ' + router_info[num]['hostname'] + '...'
    try:
        router.login()
        router_config = router.get_config()
    except:
        print 'Router get configuration error'
        print router_info[num]
        router.logout()
        sys.exit()
    else:
        router.logout()

    # Create output file written config
    try:
        output_filename = args.ouput + 'router_config/' + router_info[num]['hostname'] + '.txt'
        print 'Writing output file "' + output_filename + '"...'
    except AtributeError:
        print 'cannot read router_info[' + num + '][hostname]'
        sys.exit()

    writefile(output_filename, router_config)

    print 'Success : "'  + output_filename + '" !'
