#program to print HDFS fie to console by row
#import the following and create the infer schema
import csv 
import json 
import unicodedata 
from pyspark import SparkContext, SparkConf
import sys
sc = SparkContext("local", "Simple App")
#refer the infered schema and pull the .csv file from Hadoop cluster
input_file =sc.textFile("hdfs://localhost:9000/home/hadoop/h_data/sales_ord_univ.csv
#map the file and using utf8 format and collect into a single frame
Spark_dataframe= input_file.map(lambda line: line.encode("utf8")).collect()
hdfs_csv = csv.DictReader(Spark_dataframe)
title = hdfs_csv.fieldnames
#output to console
for row in hdfs_csv : 
	print (row  ) 

