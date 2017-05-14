# Hardcoded Json Output Spark

import csv 
import json 
import unicodedata 
from pyspark import SparkContext, SparkConf
import sys

sc = SparkContext("local", "Simple App")
def parse (line):
	fields = line.split(';')
	return (fields[0], fields[1],fields[2],fields[3].decode('ascii', 'ignore'),fields[4].decode('ascii', 'ignore') )

A =sc.textFile("hdfs://localhost:9000/home/hadoop/h_data/sales_ord_univ.csv")
B= A.map(lambda line: line.encode("utf8")).map(parse).collect()

header = A.map(parse).first() 
print header[0]
hdr_0 = header[0]
hdr_1 = header[1]
hdr_2 = header[2]
hdr_3 = header[3]
hdr_4 = header[4]

for row in B : 
	print "{"
	print hdr_0 + ":" + row[0]    + ","
	print hdr_1 + ":" +  row[1]   
	print hdr_2 + ":" +  row[2]   
	print hdr_3 + ":" +  row[3]   
	print hdr_4 + ":" +  row[4]   
	print "}"
