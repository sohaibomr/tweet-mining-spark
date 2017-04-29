# -*- coding: utf-8 -*-
"""
Created on Sat Apr 29 23:36:38 2017

@author: sohaib
"""
from pyspark import SparkContext
from pyspark.streaming import StreamingContext


#create spark context
sc=SparkContext("local[2]", "TweetAnalyser")

#create spark streaming context

ssc=StreamingContext(sc, 10)

socket_stream=ssc.socketTextStream("127.0.0.1", 8888)

lines=socket_stream.window(20)
hash_tags=(lines.flatMap(lambda line: line.split(" ")).filter(lambda word: word.lower().startswith("#"))
.map(lambda word:(word.lower(), 1))
.reduceByKey(lambda x,y: x+y)
)



hash_tags.pprint()

ssc.start()             # Start the computation
ssc.awaitTermination()  # Wait for the computation to terminate
