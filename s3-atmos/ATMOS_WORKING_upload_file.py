#!/usr/bin/python 

import ConfigParser
import boto.s3.connection

v_provider = 'skyscape'
v_credsfile = '/root/s3_api/.aws/credentials'
v_conffile = '/root/s3_api/.aws/config'
v_host = 'cas00003.skyscapecloud.com'
v_port = '8443'

# read S3 bucket auth info from .aws/credentials
creds = ConfigParser.ConfigParser()
creds.read(v_credsfile)

# read S3 bucket auth info from .aws/config
config = ConfigParser.ConfigParser()
config.read(v_conffile)

#read from .aws/credentials
aws_access_key_id = creds.get( (v_provider), "aws_access_key_id")
aws_secret_access_key = creds.get( str(v_provider), "aws_secret_access_key")
bucket = creds.get( str(v_provider), "bucket")

#read from .aws/config
host = config.get( str(v_provider), "host")


conn = boto.connect_s3(

        aws_access_key_id = (aws_access_key_id),

        aws_secret_access_key = (aws_secret_access_key),

        host = (v_host),

        port = int(v_port),

        calling_format = boto.s3.connection.OrdinaryCallingFormat(),

           )

from boto.s3.key import Key

b = conn.get_bucket(bucket)
k = Key(b)
k.key = 'ruby.rb'
k.set_contents_from_filename('/root/s3_api/ruby.rb')


