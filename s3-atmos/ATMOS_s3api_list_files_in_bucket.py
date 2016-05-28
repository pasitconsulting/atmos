#!/usr/bin/python

import boto3

AWS_ACCESS_KEY_ID = '0d5f8c93737d4e82b95254083f30594d/A6352552154f0b04a38c'
AWS_SECRET_ACCESS_KEY = '9+DFQyvChotHSCFrjJaWLAYh/A8='

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

#list files in a bucket
client = boto3.client('s3')
mylist = client.list_objects(Bucket='test-testy-test-test')

print mylist
