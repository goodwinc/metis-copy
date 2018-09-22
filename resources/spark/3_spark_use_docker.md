#Using Docker for Spark and Jupyter Notebook 

####Run the Docker Container
**Note:**  
- make sure all other Jupyter notebook sessions have been shut down
- launch the notebook from your home directory (Ex:  `/Users/reshamashaikh/`)
- type the syntax _exactly_ as it appears below (no need to change the `/home/joyvan/work` directory)

```bash
$ docker run -d -p 8888:8888 -v $PWD:/home/jovyan/work --name spark jupyter/pyspark-notebook
```

####Open Browser
Open a browser to **[http://localhost:8888](http://localhost:8888)** and you will see the Jupyter home page.

---
##Helpful Docker commands

####Stop a Docker container from running in the background
```bash
$ docker stop spark
```
####To start the Docker container again
```bash
$ docker start spark
```
####To remove the Docker container altogether
```bash
$ docker rm spark
```


####Check to see if any Docker processes running
```bash
$ docker ps
```

####Check all Docker processes
```bash
$ docker ps -a
```

####To remove a Docker proces
```bash
$ docker rm [name]
```

---

##References

[Docker error response from daemon: Conflict. already in use by container](http://stackoverflow.com/questions/31676155/docker-error-response-from-daemon-conflict-already-in-use-by-container)


