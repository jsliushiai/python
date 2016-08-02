#!/bin/bash
/service/mysql5/bin/mysqladmin -uroot -p'idontcare' extended-status |awk '
/Queries/{q=$4}/Com_commit/{c=$4}/Com_rollback/{r=$4}/Threads_connected/{tc=$4}/Threads_running/{tr=$4}END{printf("%d %d %d %d %d\n",q,c,r,tc,tr)}' >> /root/mysqlstatus_`date +%Y-%m-%d`.log