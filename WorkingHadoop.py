import csv 
import json 
import unicodedata 
from pyspark import SparkContext, SparkConf
import sys

sc = SparkContext("local", "Simple App")

A =sc.textFile("hdfs://localhost:9000/home/hadoop/h_data/sales_ord_univ.csv")
B= A.map(lambda line: line.encode("utf8")).collect()

hdfs_csv = csv.DictReader(B)
title = hdfs_csv.fieldnames
	
for row in hdfs_csv : 
	print (row  ) 

