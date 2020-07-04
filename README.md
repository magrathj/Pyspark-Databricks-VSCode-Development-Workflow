# Pyspark-Databricks-VSCode-Development-Workflow
Setting up a pyspark development workflow between VSCode and Databricks. So that, a developer can develop tests and run pyspark code locally, before deploying it to databricks. Allowing for developer to utilise test driven development in VSCode before migrating to notebooks in Databricks.  


### Pyspark development locally using docker instance

```
    docker pull mcr.microsoft.com/mmlspark/release
```

```
   docker run -it -p 8888:8888 -e ACCEPT_EULA=yes mcr.microsoft.com/mmlspark/release
```

```
    pip install -r requirements.txt 
```


### Pypsark development using Databricks-connect

