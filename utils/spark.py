"""
spark.py
~~~~~~~~

Módulo de funções auxiliares para Apache Spark
"""

from pyspark.sql import SparkSession


def start_spark(app_name='my_spark_app'):
    """Recupera ou cria uma sessão do Spark.

    :param app_name: Nome da aplicação Spark.
    :return: Spark Session.
    """

    spark = SparkSession.builder \
        .appName(app_name) \
        .getOrCreate()

    return spark
