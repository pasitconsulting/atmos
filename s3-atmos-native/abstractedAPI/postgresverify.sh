#!/bin/bash 

# Set up uid, key, and endpoint
uid="0d5f8c93737d4e82b95254083f30594d/A6352552154f0b04a38c"
key="9+DFQyvChotHSCFrjJaWLAYh/A8="
endpoint="https://cas00003.skyscapecloud.com"

#force pass in of 1 runtime parameter
if [ $# -ne 1 ]
then
  echo "i need a filename passing in as a runtime parameter"
  exit
else
  echo ""
  echo "postgresverify.sh runtime is $1"
  echo ""
  sleep 5
  verifyfile=$1
fi

#download file from object store
/root/bash_api/api-readobject.sh $verifyfile | dos2unix   | sed '1,14d' > /tmp/read.txt

#perform an md5 check on downloaded file
newmd5check=`/usr/bin/md5sum /tmp/read.txt  | awk '{print $1}' `



#read stored md5file md5check from metatag
atmosmd5sum=`/root/bash_api/api-metadata-get.sh $1 | grep listable | awk '{print $2}' | cut -c10-41`

#compare object store file md5 metatag with fresh md5check
echo "atmosmd5sum $atmosmd5sum"
echo "newmd5check $newmd5check"

if [ "$atmosmd5sum" = "$newmd5check" ]
then
  echo "checksums match, file /tmp/read.txt upload verification succeeded"
  exit
else
  echo "checksums DO NOT match, please re-upload the file to atmos"
  exit
fi



