import findspark
import os
from pyspark import SparkContext

os.environ["HADOOP_HOME"] = "C:/opt/apache-spark"

try:
    findspark.init()
    spark = SparkContext()

    lista = [1,2,3,4,5]
    lista_rdd = spark.parallelize(lista) 

    print(lista_rdd.count())
finally:
    spark.stop()