# Pyspark-Databricks-VSCode-Development-Workflow

## Introduction

![Python package](https://github.com/magrathj/Pyspark-Databricks-VSCode-Development-Workflow/workflows/Python%20package/badge.svg)

This repo is setting up a pyspark development workflow between VSCode and Databricks to bridge the gap between testing pyspark packages before deploying them to databricks using databricks-connect or the databricks APIs. 

Specifically, to solver a wider issue - when building out a pyspark application, a lot of the time can be spent building out code in isolation which we can package up. However, this typically means using databricks-connect and requires you to have a cluster available while you build out the application. In larger projects where you have a large team working on a databricks workspace these costs can amount to quite a bit. Whereas, if you isolate your code to individual components and packaged them up locally in VScode then you dont need to incur cluster costs to build out and test a small component. The later you can integrate those packages and get the benefit of distributed computing. 


To give you an idea of the cost problem, if you had a team of five developers building out their application on one databricks development workspace with low spec cluster for circa 170 hours a month (40 hours per week x 52 weeks per year / 12 months per year = 173.33 average monthly hours) then you are looking at a pay as you go cost of over $10k a month. ![azure databricks cost calculator](https://azure.microsoft.com/en-gb/pricing/calculator/?service=databricks) 

![cost_calculator](./images/cost_calculator.PNG)



***Packages*** -> unit tested locally or on remote servers using spark-mml package

***Databricks notebooks using the packages*** -> tested using databricks-connect to deploy the packages to the cluster and consume them in a notebook 


The project is designed for:

    Python local development in an IDE (VSCode) using pyspark and spark-mml 
    Simple data pipelines with reusable code
    Unit Testing with Pytest
    Build into a Python Wheel
    CI Build with Test results published
    Automated deployments/promotions


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
