#!/bin/bash
#
# Author : hhl
#
# email : dnrhhl@gmail.com
#
# Time : 二 27 3月 2018 20:17:44
#
#
a_list=( 0.1 0.08 0.05 0.01)
num=${#a_list[@]}

for((i=0;i<num;i++))
{
  echo ${a_list[i]};
}

for a in ${a_list[*]}
do
  echo $a
done
