"""
etl.py
~~~~~~~~~~

Módulo com a definição do job ETL para coleta e
transformação do histórico do índice CDI.
"""

from pyspark.sql import functions as F, Window, types

from functools import reduce
from operator import mul
import datetime

from utils import cdi, dates
from utils.spark import start_spark


def main():
    """Definição do pipeline.

    :return: None
    """

    # Inicia a aplicação Spark e recupera uma Spark Session
    spark = start_spark(app_name="mr-data-test")

    # definição do período
    start = datetime.datetime(1994, 7, 4)
    end = datetime.datetime(2021, 7, 26)

    dates_list = dates.list_generate(start, end)

    # execução do pipeline
    data = extract_data(spark, dates_list)
    data_transformed = transform_data(data)
    load_data(data_transformed)

    # encerra a aplicação Spark
    spark.stop()


def extract_data(spark, dates_list):
    """Recupera o índice do CDI para
        cada dia do perído.

    :param spark: Spark Session.
    :return: Spark DataFrame.
    """

    rdd = spark.sparkContext.parallelize(dates_list)

    rdd = rdd.map(cdi.get_fator)

    df = spark.createDataFrame(rdd)

    return df


def transform_data(df):
    """Calcula o Fator Acumulado e
        a Taxa Acumulada.

    :param df: Spark DataFrame.
    :return: Spark DataFrame.
    """

    df_transformed = df.withColumn("Fator", df["Fator"].cast('double'))
    df_transformed = df_transformed.withColumn(
        "Data", df_transformed["Data"].cast('date'))

    window = Window.orderBy('Data')
    mul_udf = F.udf(lambda x: reduce(mul, x), types.DoubleType())
    df_transformed = df_transformed.withColumn(
        'FatorAcumulado', mul_udf(F.collect_list(F.col('Fator')).over(window)))

    df_transformed = df_transformed.withColumn(
        'TaxaAcumulada', (100 * (df_transformed["FatorAcumulado"] - 1)))

    return df_transformed


def load_data(df):
    """Armazena os dados em uma tabela delta.

    :param df: Spark DataFrame.
    :return: None
    """

    df.write.format("delta").mode("overwrite").save(
        "/tmp/spark_output/delta-table")

    return None


# ponto de entrada da aplicação
if __name__ == '__main__':
    main()
