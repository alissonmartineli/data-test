FROM bde2020/spark-python-template:3.1.1-hadoop3.2

LABEL maintainer="Alisson Martineli <martineli.alisson@gmail.com>"

ENV SPARK_APPLICATION_PYTHON_LOCATION /app/jobs/etl.py
ENV SPARK_SUBMIT_ARGS "--packages io.delta:delta-core_2.12:1.0.0 --py-files /app/packages.zip"
