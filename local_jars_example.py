from pyspark.sql import SparkSession

spark = SparkSession.builder\
        .appName("Sample Jars Application")\
        .config("spark.jars", "/opt/spark/examples/jars/spark-examples.jar,/opt/spark/examples/jars/scopt_2.12-3.7.1.jar")\
        .config("spark.driver.extraClassPath", "/opt/spark/examples/jars/spark-examples.jar,/opt/spark/examples/jars/scopt_2.12-3.7.1.jar")\
        .config("spark.executor.extraClassPath", "/opt/spark/examples/jars/spark-examples.jar,/opt/spark/examples/jars/scopt_2.12-3.7.1.jar")\
        .getOrCreate()
      
spark.sparkContext.getConf().getAll()

#spark.stop()

