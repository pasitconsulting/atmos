#!/bin/bash  -x 

################
#SET ACL
################

# Set up uid, key, and endpoint
uid="0d5f8c93737d4e82b95254083f30594d/A6352552154f0b04a38c"
key="9+DFQyvChotHSCFrjJaWLAYh/A8="
endpoint="https://cas00003.skyscapecloud.com"
date=`date -u +"%a, %d %b %Y %H:%M:%S GMT"`
subtenantid="0d5f8c93737d4e82b95254083f30594d"

useracl="viewbackups=READ, writebackups=WRITE, adminbackups=FULL_CONTROL" 
groupacl="grouptest=READ" 

# Choose the file to upload
pgbackupdir="/opt/postgresqlbkdumps"
latestpgbackup="`ls -at $pgbackupdir | head -n 1`"
file_to_upload="$pgbackupdir/$latestpgbackup"

# Choose the Atmos directory
atmos_dir="/postgres/"

# Build and send the Atmos request
filename=`basename $file_to_upload`
atmos_path="/rest/namespace${atmos_dir}$filename?acl"

contentType="application/octet-stream"

signstr="POST\n${contentType}\n\n\n${atmos_path}\nx-emc-date:${date}\nx-emc-groupacl:$groupacl\nx-emc-uid:${uid}\nx-emc-useracl:$useracl"

sig=$(python -c "import base64, hmac, sha; print base64.b64encode(hmac.new(base64.b64decode(\"$key\"), \"$signstr\", sha).digest())")

curl -i -X POST  \
     -H "Content-Type:$contentType"   \
     -H "x-emc-date:$date"     \
     -H "x-emc-groupacl:$groupacl"  \
     -H "x-emc-uid:$uid"    \
     -H "x-emc-useracl:$useracl"  \
     -H "x-emc-signature:$sig"    \
 --data-binary @${file_to_upload} ${endpoint}${atmos_path}

