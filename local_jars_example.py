from pyspark.sql import SparkSession

spark = SparkSession.builder\
        .appName("MySQL Connection")\
        .config("spark.jars", "/opt/spark/examples/jars/spark-examples.jar,/opt/spark/examples/jars/scopt_2.12-3.7.1.jar")\
        .getOrCreate()
      
spark.sparkContext.getConf().getAll()

spark.stop()