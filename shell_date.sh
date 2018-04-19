#!/bin/bash
#
# Author : hhl
#
# email : dnrhhl@gmail.com
#
# Time : 四 19 4月 2018 11:16:34
#
#
start_day_str=$1
end_day_str=$2
day_2_ago8_str=$3
start_day=$(date -d "$start_day_str" +%Y%m%d)
end_day=$(date -d "$end_day_str" +%Y%m%d)
day_2_ago8=$(date -d "$day_2_ago8_str" +%Y%m%d)

while [ $end_day -lt $start_day ]
do
    start_day=$(date -d "$start_day 1 days ago" +%Y%m%d)
    echo $start_day
done


