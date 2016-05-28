#!/usr/bin/python 

#import sys
import boto.s3
import boto.s3.connection

# read S3 bucket auth info from conf file
import ConfigParser
creds = ConfigParser.ConfigParser()
creds.read("/root/s3_api/.aws/credentials")

config = ConfigParser.ConfigParser()
config.read("/root/s3_api/.aws/config")

provider = 'skyscape'

aws_access_key_id = creds.get( (provider), "aws_access_key_id")
aws_secret_access_key = creds.get( str(provider), "aws_secret_access_key")
host = config.get( str(provider), "host")


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
k = Key(b)
k.key = 'ruby.rb'
k.set_contents_from_filename('/root/s3_api/ruby.rb')


