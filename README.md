# Pyspark-Databricks-VSCode-Development-Workflow
Setting up a pyspark development workflow between VSCode and Databricks. So that, a developer can develop tests and run pyspark code locally, before deploying it to databricks. Allowing for developer to utilise test driven development in VSCode before migrating to notebooks in Databricks.  


## Setup

``` bash
    conda create --name dbconnectapp python=3.7
```

``` bash
    conda activate dbconnectapp 
```

``` bash
    pip install -r requirements.txt
```

``` bash
    databricks-connect configure
```

