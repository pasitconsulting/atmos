#!/bin/bash

###############
#BESPOKE BACKUP
###############

echo "location of directory to backup: "
read location

echo ""
echo "i will backup $location"
echo ""
sleep 3

filename="`hostname -s`"-"`date +\%Y%m%d%H%M%S`.tar"

/usr/bin/tar -cvf /tmp/$filename $location
/usr/bin/gzip /tmp/$filename

echo ""
echo "created tar of $location:  /tmp/$filename.gz"
echo ""
sleep 5


#upload backup to skyscapestorage
/root/bash_api/api-filecreate.sh /tmp/$filename.gz

#call the md5check 
/opt/abstractedAPI/postgresverify.sh /tmp/$filename.gz
