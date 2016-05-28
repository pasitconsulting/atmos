#!/usr/bin/python

import boto3

AWS_ACCESS_KEY_ID = 'AKIAIYPYWDEYCHF3MMSA'
AWS_SECRET_ACCESS_KEY = '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'

mybucket="test-testy-test-test"
myfile="dogsblx"



#instantiate sessions
default = boto3.Session(profile_name='default')
skyscape = boto3.Session(profile_name='skyscape')

#assign s3 name variable to existing sessions
default_session = default.resource('s3')
skyscape_session = skyscape.resource('s3')

#define objects
bucket_default = default_session.Object(bucket_name=str(mybucket), key=(myfile) )
bucket_skyscape = skyscape_session.Object(bucket_name=str(mybucket), key=(myfile) )

#instantiate a resource
default_resource = boto3.resource('s3')

#upload = boto3.s3.inject.upload_file( (myfile) , (bucket_default), (myfile), ExtraArgs=None )
#boto3.s3.inject.bucket_upload_file
#default_resource.session.client.upload_file('/root/s3_api/ruby.rb', '(mybucket)', 'ruby.rb')

s3_client = boto3.client('s3')
s3_client.upload_file( '/root/s3_api/ruby.rb' , (mybucket), 'ruby.rb' )
