#!/usr/bin/python

import boto3

AWS_ACCESS_KEY_ID = 'AKIAIYPYWDEYCHF3MMSA'
AWS_SECRET_ACCESS_KEY = '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'

mybucket="test-testy-test-test"
myfile="dogsblx"



#define session
default = boto3.Session(profile_name='default')
skyscape = boto3.Session(profile_name='skyscape')

#define resource
default_resource = default.resource('s3')
skyscape_resource = skyscape.resource('s3')

#define objects
bucket_default = default_resource.Object(bucket_name=str(mybucket), key=(myfile) )
bucket_skyscape = skyscape_resource.Object(bucket_name=str(mybucket), key=(myfile) )

print (bucket_default)

#transfer file from S3 to local
s3 = boto3.resource('s3')
s3.meta.client.download_file( (mybucket), 'ruby.rb', './ruby.rb.downloaded')
