# Pyspark-Databricks-VSCode-Development-Workflow

![Python package](https://github.com/magrathj/Pyspark-Databricks-VSCode-Development-Workflow/workflows/Python%20package/badge.svg)

Setting up a pyspark development workflow between VSCode and Databricks, to bridge the gap between testing pyspark packages and then deploying them to wider databricks applications which consume them. 

Typically, developers build out their pyspark packages and use databricks-connect to deploy their package. They then test the package once its been installed onto a databricks cluster. I wanted to change the workflow slightly to test packages in isolation, as building them out as packages should allow them to be completely modular to your complete application, and then run integration tests with your wider application consuming the pyspark package. 

Packages -> unit tested locally or on remote servers
Databricks notebooks using the package -> tested using databricks-connect to deploy the packages and consume them 



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
