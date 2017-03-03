#!/bin/bash

cp /var/log/kern.log ./mylogs.log
cat mylogs.log | awk '{print $8}' > ./mylogs_clean.log
python inversion_counter_1.py
#./algo array_input



