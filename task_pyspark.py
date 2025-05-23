from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder.getOrCreate()

products = spark.createDataFrame([
    (1, "Кола"),
    (2, "Виски"),
    (3, "Каша"),
    (4, "Гантели")
], ["product_id", "product_name"])

categories = spark.createDataFrame([
    (5, "Продуктовый"),
    (8, "Бар"),
], ["category_id", "category_name"])

product_categories = spark.createDataFrame([
    (1, 5),
    (1, 8),
    (2, 5),
    (2, 8),
    (3, 5),
], ["product_id", "category_id"])


prod_cat = products.join(product_categories,on="product_id",how="left") \
                    .join(categories,on="category_id", how="left") \
                    .select("product_name","category_name")

prod_cat.show()