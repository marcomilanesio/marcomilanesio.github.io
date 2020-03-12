# EXAM

Implement the WordCount algorithm using the SparkDataframe API (pyspark.sql).
Use the file 'sample.txt' for testing.

Necessary steps:
1 - load the text file into a dataframe of 2 columns: ["word", "count"]
2 - Return the top10 most frequent words.


## HINT:  `pyspark.sql.functions.explode(col)` Returns a new row for each element in the given array or map.

https://spark.apache.org/docs/latest/api/python/pyspark.sql.html?highlight=explode

## REMINDER:
Plug this at the beginning of the Colab notebook.

```
!apt-get install openjdk-8-jdk-headless -qq > /dev/null
import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-8-openjdk-amd64"
!update-alternatives --set java /usr/lib/jvm/java-8-openjdk-amd64/jre/bin/java
!java -version
!pip install pyspark
```

### To upload the file: 
```
from google.colab import files
files.upload()  # and navigate to your 'sample.txt'
```
