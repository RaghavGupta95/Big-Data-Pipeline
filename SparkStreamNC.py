# Simple Netcat Streaming Program
# Start Netcat host on a different tab/window with "nc -lk 7792" Start a local netcat at port no. 7792 
# Spark Submit this program within the current directory as " spark-submit SparkStreamNC.py localhost 7792"

from pyspark import SparkContext
from pyspark.streaming import StreamingContext
#from pyspark.streaming.flume import FlumeUtils



#addresses = (["localhost"], [4444]) #([sink machine hostname 2], [sink port 2])]
#flumeStream = FlumeUtils.createPollingStream(StreamingContext, addresses)
# Create a local StreamingContext with two working thread and batch interval of 100 second
sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 10)# the number denotes the amount after which the script will refresh for a new batch.


# Create a DStream that will connect to hostname:port, like localhost:9999
lines = ssc.socketTextStream("localhost", 7792)

# Do the following split on the Dstream and print out the input 
words = lines.flatMap(lambda line: line.split(" "))
pairs = words.map(lambda word: (word, 1))
wordCounts = pairs.reduceByKey(lambda x, y: x + y)
wordCounts.pprint()
# Start the streaming context 
ssc.start()
ssc.awaitTermination()
