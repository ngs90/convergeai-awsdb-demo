# Databricks notebook source
def add(a, b):

    return a + b

add(5, 2)

# COMMAND ----------

df = spark.table('convergeai_dev.default.employee_lab')
df.show(5)

# COMMAND ----------
