# Working with Spark Jars in CML

### Objective

There are multiple ways to add jars to a PySpark application. This repository provides two basic examples.


### Requirements

This tutorial requires basic knowledge of Python and PySpark and a CML Workspace where to deploy the project.


### Project Setup

Step 1: Create a CML Project by cloning this github repository. All files will be loaded into the CML Project automatically.

Step 2: Start a CML Session with the following configurations:

```
Editor: Workbench
Kernel: Python 3.7 or above
Edition: Standard
Enable Spark: Version 2.4.8
Resource Profile: 1 vCPU / 2 GiB Memory - 0 GPUs
```

Step 3: In the open CML Session prompt, run the following command to install the necessary dependencies:

```!pip3 install -r requirements.txt```


### Option 1: Load Jars from Local Folders

You can load jar from the local project filesystem into a Spark Session in CML. For example you may have to use a JDBC Driver to connect to a Postgres Database.

Open ```local_jars_example.py```, familiarize yourself with the code and run the entire script.

* The example uses the ```spark.jars``` option at line 5 to load two jars located in ```/opt/spark/examples/jars/```.
* These jars are already present in CML at project deployment but if you would like to use yours you can simply edit the file path and manually load the jars to the designated folder.


### Option 2: Load Jars from Maven

Some open source libraries are not available via a simple pip install. This is the case for [MMLSpark](https://mmlspark.blob.core.windows.net/website/index.html#install), a Spark module with many machine learning algorithms and transformers going beyond SparkML.

In these circumstances you may have to load your packages from Maven.

Open ```maven_jars_example.py```, familiarize yourself with the code and run the entire script.

* The example uses the ```spark.jars.packages``` and ```spark.jars.repositories``` at lines 6 and 7 to load the jars directly in the Spark Session from Maven.
* Typically your Spark module documentation will provide the necessary Maven coordinates for the two Spark options. In general you can locate these coodinates directly from the Maven site.


# Conclusions & Next Steps

This tutorial has provided two examples of using Spark Jars in CML. If you use CML you may also benefit from testing the following demos:

* [Telco Churn Demo](https://github.com/pdefusco/CML_AMP_Churn_Prediction): Build an End to End ML Project in CML and Increase ML Explainability with the LIME Library
* [Learn how to use Cloudera Applied ML Prototypes](https://docs.cloudera.com/machine-learning/cloud/applied-ml-prototypes/topics/ml-amps-overview.html) to discover more projects using MLFlow, Streamlit, Tensorflow, PyTorch and many more popular libraries
* [CSA2CML](https://github.com/pdefusco/CSA2CML): Build a real time anomaly detection dashboard with Flink, CML, and Streamlit
* [SDX2CDE](https://github.com/pdefusco/SDX2CDE): Explore ML Governance and Security features in SDX to increase legal compliance and enhance ML Ops best practices
* [API v2](https://github.com/pdefusco/CML_AMP_APIv2): Familiarize yourself with API v2, CML's goto Python Library for ML Ops and DevOps
* [MLOps](https://github.com/pdefusco/MLOps): Explore a detailed ML Ops pipeline powered by Apache Iceberg
