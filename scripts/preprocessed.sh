#!/bin/bash

timestamp=$(date "+%Y%m%d_%H%M")
filename="../data/processed/sales_processed_${timestamp}.csv"
mkdir -p ../data/processed
touch "$filename"

python3 ../src/preprocessed.py >> "$filename"

echo "[$timestamp]: preprocessed file >> ../logs/preprocessed.logs"
