# Coletando e transformando dados do CDI

Pipeline para coleta e transformação do histórico do índice CDI utilizando como fonte de dados a calculadora da B3 disponibilizada em https://calculadorarendafixa.com.br/.

## Executando localmente

```
$SPARK_HOME/bin/spark-submit \
    --master local \
    --packages io.delta:delta-core_2.12:1.0.0 \
    --py-files packages.zip \
    jobs/etl.py
```

## Executando no docker

```
# iniciando os containers
docker compose up -d

# construindo a imagem da aplicação Spark
docker build -t alissonmartineli/mr-data-test .

# executando a aplicação Spark
docker run --rm \
 --name mr-data-test \
 -e ENABLE_INIT_DAEMON=false \
 --link spark-master:spark-master \
 --net mr-data-test-network \
 -v mr-data-test-workspace:/tmp/spark_output \
 alissonmartineli/mr-data-test

# listando o resultado
docker exec -it spark-master ls /tmp/spark_output/delta-table
```

# Resultado

A saída do processo é uma tabela delta gravada no caminho /tmp/spark_output/delta-table.

O resultado previamente gerado esta armazenado na pasta output deste projeto.

# Dependências

O arquivo packages.zip contém as dependências necessárias para execução do pipeline.

O arquivo foi gerado a partir do processamento contido no arquivo build_dependencies.sh.

# Notebook

O arquivo mr_data_test.ipynb contém o notebook com a POC do pipeline.
