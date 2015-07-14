#! /usr/bin/env python
import sys
import json

def readfile(filename):
    try:
        file = open(filename, 'r')
    except ( IOError, IndexError):
        print 'Cannot open file : ' + filename
        sys.exit()
    output_str  = file.read()
    file.close()
    return output_str

def writefile(filename, output_str):
    try:
        file = open ( filename, 'w')
    except:
        print 'cannot open "' + filename + '"'
        file.close
        sys.exit()
    file.write( output_str )
    file.close

def convert_jason_to_dict( input_json ):
    try:
        output_dict = json.loads( input_json )
    except ValueError as error:
        print 'JSON format error : '
        print  input_json
        print error
        sys.exit()
    return output_dict
