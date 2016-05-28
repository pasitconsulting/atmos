#!/bin/bash

#POSTGRES VARIABLES
pgconf="/var/lib/pgsql/data/postgresql.conf"
pgbkdir="/opt/postgresqlbkdumps"
#filename="`hostname -s`"-"`date +\%Y%m%d%H%M%S`"
pgfilename="pgauto`date +\%Y%m%d%H%M%S`"


if [ -f $pgconf ]
then
 #we have a postgres database
 /usr/bin/pg_dumpall > /opt/postgresqlbkdumps/postgresbackup`date +\%d%m%y_%M%S`
 latestpgbackup="`ls -t $pgbkdir | head -n 1`"
 /usr/bin/tar -cvzf $pgbkdir/$latestpgbackup.tar.gz $pgbkdir
fi


#upload backup to skyscapestorage
/root/bash_api/api-filecreate.sh $pgbkdir/$latestpgbackup.tar.gz

#call the md5check
/root/bash_api/abstractedAPI/postgresverify.sh $pgbkdir/$latestpgbackup.tar.gz
