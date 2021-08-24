from pyspark.sql import SparkSession
from pyspark.sql.functions import col,date_format

def init_spark():
  spark = SparkSession.builder\
    .appName("datalake-app")\
    .getOrCreate()

  sc = spark.sparkContext

  #sc._jsc.hadoopConfiguration().set("fs.azure.account.key.mhtestdatalake.dfs.core.windows.net", "FKj74Eg5JoTM9x/7AxSNjV+DQ0lKKeo63Y+iamG6uLbJ+YRa4kIPAp5Z/r7IlnziDOEoa7SZmA8Mg7ATrMRKHw==")

  return spark,sc

def main():

  spark,sc = init_spark()

  rdd = sc.textFile("abfs://raw@mhtestdatalake.dfs.core.windows.net/cosmos-spark.txt")
  print(rdd.count())
  
if __name__ == '__main__':
  main()