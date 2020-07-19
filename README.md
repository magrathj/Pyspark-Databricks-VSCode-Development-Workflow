# Pyspark-Databricks-VSCode-Development-Workflow
Setting up a pyspark development workflow between VSCode and Databricks. So that, a developer can develop tests and run pyspark code locally, before deploying it to databricks. Allowing for developer to utilise test driven development in VSCode before migrating to notebooks in Databricks.  


### Pyspark development locally

```
    conda create --name localdevelopment python=3.7
```

```
    conda activate localdevelopment
```

```
    pip install -r local_development_requirements
```


### Pypsark development using Databricks-connect



```
    conda create --name databricksdevelopment python=3.7
```

```
    conda activate databricksdevelopment
```

```
    pip install -r databricks_connect_requirements.txt
```


#### Configure Library

At prompt run:

```
    databricks-connect configure
```

Complete the questions - they are pretty straightforward. Once done you can run this command to test:

```
    databricks-connect test
```

If you get any errors check the troubleshooting section. But hopefully you are good to go.

[databricks-connect-development](https://datathirst.net/blog/2019/3/7/databricks-connect-finally)




### Pyspark development locally using docker instance (for notebooks)

```
    docker pull mcr.microsoft.com/mmlspark/release
```

```
   docker run -it -p 8888:8888 -e ACCEPT_EULA=yes mcr.microsoft.com/mmlspark/release
```
