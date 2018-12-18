#!/bin/bash
# test.sh
 
MAX=110

for (( i = 0; i < MAX ; i ++ ))
do
    echo ${i}
    time curl -H "Host: helloworld-python.default.example.com" http://119.28.33.55

    time curl -H "Host: blue-green-demo.default.example.com" http://119.28.33.55
done


