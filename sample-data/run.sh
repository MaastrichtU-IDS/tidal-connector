#! /bin/bash

############################
# NOTICE: The Lung1 data is licensed not for commercial use!
# more information: https://wiki.cancerimagingarchive.net/display/Public/NSCLC-Radiomics
############################

mkdir ./triplifier_data

curl -o ./triplifier_data/lung1.csv https://wiki.cancerimagingarchive.net/download/attachments/16056854/NSCLC%20Radiomics%20Lung1.clinical-version3-Oct%202019.csv?version=1&modificationDate=1572013183040&api=v2

docker-compose up -d
