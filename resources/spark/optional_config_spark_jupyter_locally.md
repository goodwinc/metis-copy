# Configure Spark and Jupyter Notebook, Locally

## Add paths to `bash` file

```bash
nano ~/.bashrc  (or .bash_profile)
```
#### Add the following to the end of your `.bashrc` file.   

```bash
export SPARK_HOME=$HOME/apps/spark-1.6.2-bin-hadoop2.6
export PY4J_NAME=$(basename `find $SPARK_HOME/python/lib -name 'py4j*src.zip'`)
export PYTHONPATH=$PYTHONPATH:$SPARK_HOME/python:$SPARK_HOME/python/lib/$PY4J_NAME
export PYSPARK_SUBMIT_ARGS="--master local[2]" 
```
#### source your bash file

```bash
source ~/.bashrc  (or .bash_profile)
```
## Create `pyspark` Profile

```bash 
ipython profile create pyspark
```
```bash 
nano ~/.ipython/profile_pyspark/startup/00-pyspark-setup.py
```

#### copy and paste the following into your `00-pyspark-setup.py` file.

```bash
# Configure the necessary Spark environment
import os
import sys

# Spark home
spark_home = os.environ.get('SPARK_HOME', None)

sys.path.insert(0, spark_home + "/python")

# If Spark V1.4.x is detected, then add ' pyspark-shell' to
# the end of the 'PYSPARK_SUBMIT_ARGS' environment variable
spark_release_file = spark_home + "/RELEASE"
if os.path.exists(spark_release_file) and "Spark 1.6" in open(spark_release_file).read():
    pyspark_submit_args = os.environ.get("PYSPARK_SUBMIT_ARGS", "")
    if not "pyspark-shell" in pyspark_submit_args:
        pyspark_submit_args += " pyspark-shell"
    os.environ["PYSPARK_SUBMIT_ARGS"] = pyspark_submit_args

# Add the spark python sub-directory to the path
sys.path.insert(0, spark_home + "/python")

# Add the py4j to the path.
# You may need to change the version number to match your install
sys.path.insert(0, os.path.join(spark_home, "python/lib/py4j-0.9-src.zip"))

# Initialize PySpark to predefine the SparkContext variable 'sc'
execfile(os.path.join(spark_home, "python/pyspark/shell.py"))
```

## Launch your notebook with `pyspark`!

```bash 
ipython notebook --profile=pyspark
```

---

####References

Notes:  These references are outdated (because of updated versions of Spark, etc.), but these articles were the initial reference sources.

* [Getting Started with Spark in Python](https://districtdatalabs.silvrback.com/getting-started-with-spark-in-python)
* [Configuring IPython Notebook for PySpark](http://ramhiser.com/2015/02/01/configuring-ipython-notebook-support-for-pyspark/)
