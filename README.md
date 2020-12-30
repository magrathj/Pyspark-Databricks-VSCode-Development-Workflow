# Pyspark-Databricks-VSCode-Development-Workflow

![Python package](https://github.com/magrathj/Pyspark-Databricks-VSCode-Development-Workflow/workflows/Python%20package/badge.svg)

Setting up a pyspark development workflow between VSCode and Databricks to bridge the gap between testing pyspark packages before deploying them to databricks using databricks-connect or the databricks APIs. 

To solver a wider issue - when building out a pyspark application, a lot of the time can be spent building out code in isolation which we can package up. However, this typically means using databricks-connect and requires you to have a cluster available while you build out the application. In larger projects where you have a large team working on a workspace these costs can amount to quite a bit. Whereas, if you isolate your code and develop your package locally in VScode then you dont need to incur cluster costs to build out and test a small component.  


***Packages*** -> unit tested locally or on remote servers using spark-mml package

***Databricks notebooks using the packages*** -> tested using databricks-connect to deploy the packages to the cluster and consume them in a notebook 



## Setup

Create new env

``` bash
    conda create --name ~/.env python=3.7
```

Activate new env
``` bash
    conda activate ~/.env  
```

Run Makefile to run the setup locally 
``` bash
    make all
```


## References
![create spark context without local install](https://github.com/Azure/mmlspark)

![series-developing-a-pyspark-application](https://datathirst.net/blog/2019/9/20/series-developing-a-pyspark-application)

![series-developing-a-pyspark-application-github](https://github.com/DataThirstLtd/Databricks-Connect-PySpark)
