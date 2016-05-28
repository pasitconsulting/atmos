#!/usr/bin/python 

import ConfigParser
import boto.s3.connection

provider = 'skyscape'


# read S3 bucket auth info from .aws/credentials
creds = ConfigParser.ConfigParser()
creds.read("/root/s3_api/.aws/credentials")

# read S3 bucket auth info from .aws/config
config = ConfigParser.ConfigParser()
config.read("/root/s3_api/.aws/config")

#read from .aws/credentials
aws_access_key_id = creds.get( (provider), "aws_access_key_id")
aws_secret_access_key = creds.get( str(provider), "aws_secret_access_key")
bucket = creds.get( str(provider), "bucket")

#read from .aws/config
host = config.get( str(provider), "host")


conn = boto.connect_s3(

        aws_access_key_id = (aws_access_key_id),

        aws_secret_access_key = (aws_secret_access_key),

        host = 'cas00003.skyscapecloud.com',

        port = 8443,

        calling_format = boto.s3.connection.OrdinaryCallingFormat(),

           )

from boto.s3.key import Key

b = conn.get_bucket(bucket)
k = Key(b)
k.key = 'ruby.rb'
k.set_contents_from_filename('/root/s3_api/ruby.rb')


