#!/usr/bin/ruby

require 'rubygems'
require 'fog'

connection = Fog::Storage.new({
  :provider                 => 'AWS',
  :aws_access_key_id        => '0d5f8c93737d4e82b95254083f30594d/A6352552154f0b04a38c',
  :aws_secret_access_key    => '9+DFQyvChotHSCFrjJaWLAYh/A8=',
  :host                     => 'cas00003.skyscapecloud.com',
  :port                     => '8443',
  :path_style               => 'true'
})

#Then to create a directory:

directory = connection.directories.create(
  :key    => "fog-demo-#{Time.now.to_i}", # globally unique name
  :public => true
)

#And then list directories:

p connection.directories
