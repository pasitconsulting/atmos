#!/usr/bin/python 

import sys
import boto
import boto.s3
import boto.s3.connection

aws_access_key_id = '0d5f8c93737d4e82b95254083f30594d/A6352552154f0b04a38c'

aws_secret_access_key = '9+DFQyvChotHSCFrjJaWLAYh/A8='

bucket='test-testy-test-test'


conn = boto.connect_s3(

        aws_access_key_id = (aws_access_key_id),

        aws_secret_access_key = (aws_secret_access_key),

        host = 'cas00003.skyscapecloud.com',

        port = 8443,

        calling_format = boto.s3.connection.OrdinaryCallingFormat(),

           )

from boto.s3.key import Key

b = conn.get_bucket( 'test-testy-test-test' )


key = b.get_key('ruby.rb')

fp = open("ruby.rb", "wb")

key.get_file(fp)
