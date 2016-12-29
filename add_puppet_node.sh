#!/bin/bash
if [ -z $1 ];then
echo "Error! You must use like this:[./add_node.sh *.pp]"
exit
fi
cat ip.txt|grep -v ^#|grep -v ^$|while read line
do
ip3=`echo $line|awk -F. '{print$3}'`
ip4=`echo $line|awk -F. '{print$4}'`
#echo $ip3
#echo $ip4
node_name=`echo $1|awk -F. '{print$1}'`
echo -e " node $node_name-$ip3-$ip4 inherits $node_name {\n\n\n}\n" >>$1
done
