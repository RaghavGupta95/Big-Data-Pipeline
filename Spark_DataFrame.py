# run the program using ' spark-submit "program name" '
# import following modules 
import pymongo   # python mongo connector 
import pymongo_spark # import spark module for pymongo 
import json   # import json format
from pymongo import MongoClient # import the Mongoclient, to connect to the database 
from pyspark import SparkContext, SparkConf  # import spark contexts
from pyspark.sql import SQLContext   # import the sql context for spark
from pyspark.sql import SparkSession # run a spark session



pymongo_spark.activate() # activate the pymongo-spark connector
conf = SparkConf() # define spark configuration
sc = SparkContext(conf=conf) 
sqlContext=SQLContext(sc) 
client = MongoClient()  # define our client to be from MongoClient() server
db = client.test # define current database db as the 'test' database on the MongoClient()
print ( 'database  ',  db)  # print current database in use
path = "hdfs://localhost:9000/home/hadoop/h_data/sales_ord_univ.csv" # define the HDFS file path 
df=sqlContext.read.format("com.databricks.spark.csv").option("header", "true").option("inferSchema", "true").load(path) # Use the path to create a spark SQL dataframe 'df' using  the infered schema. 
df_pandas = df.toPandas() # Create a pandas DataFrame from the SQL Dataframe
records=json.loads(df_pandas.T.to_json()).values() # Create a json format of the dataframe 
db.test76.insert(records)  # insert the json format "records " in our current mongo database "db' under the name of "test2"
