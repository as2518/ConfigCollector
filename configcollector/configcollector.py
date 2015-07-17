# -*- coding: utf-8 -*-
import sys
from argparse import ArgumentParser
import json
from router import Router


def main():
    # Parse argment
    parser = ArgumentParser(
        description='Collect configuration files on mutiple routers')
    parser.add_argument('-i', '--inventory',
                        type=str,
                        default='/etc/configcollector/inventory.json',
                        help='router information file\n\
                        (default=etc/configcollector/inventory.json)')
    parser.add_argument('-o', '--output',
                        type=str,
                        default='./',
                        help='output directory\n\
                        (default=CURRENT_DIRECTORY)')
    args = parser.parse_args()

    # Read router infomation file
    try:
        with open(args.inventory, 'r') as file:
            router_info_json = file.read()
    except (IOError, IndexError):
        sys.stderr.write('Cannot open file : ' + args.inventory + '\n')
        sys.exit(1)

    # Convert json format to dictionary
    try:
        router_info = json.loads(router_info_json)
    except ValueError as error:
        sys.stderr.write('JSON format error : \n')
        sys.stderr.write(router_info_json)
        sys.stderr.write(str(error))
        sys.exit(1)

    # Login and get config for each routers
    for num in range(len(router_info)):
        router = Router(router_info[num])
        print('Accessing router: ' + router_info[num]['hostname'] + '...')

        try:
            router.login()
            output = router.get_config()
        except:
            sys.stderr.write('SSH connection error\n')
            sys.stderr.write(str(router_info[num]) + '\n')
            router.logout()
            sys.exit(1)
        else:
            router.logout()

        # Open output file written config
        try:
            output_filename =\
                args.output + router_info[num]['hostname'] + '.txt'
            print('Writing output file "' + output_filename + '"...')
        except AttributeError:
            sys.stderr.write('Cannot read : ' + output_filename + '\n')
            sys.exit(1)

        # Write output file
        try:
            with open(output_filename, 'w') as file:
                file.write(output)
        except:
            sys.stderr.write('Cannot open "' + output_filename + '"\n')
            file.close()
            sys.exit(1)

        print('Success : "' + output_filename + '"!')

if __name__ == '__main__':
    main()
