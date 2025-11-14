#!/bin/bash

API_URL="http://0.0.0.0:5000"

timestamp=$(date "+%Y%m%d_%H%M")
filename="../data/raw/sales_${timestamp}.csv"
touch "$filename"
echo "timestamp,model,sales" >> "$filename"

while read model;
do
    sales=$(curl  "${API_URL}/${model}")
    echo "${timestamp},${model},${sales}" >> "$filename"

echo "[$timestamp]: Model=${model}, Sales= ${sales}" >> ../logs/collect.logs
done < ../data/model_list.txt
