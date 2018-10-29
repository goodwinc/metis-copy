### mongoDB on Ubuntu: for use on AWS, for example. 

This is a great way to do things if you want a cloud-based database for large amounts of storage or for nice integration with a live streaming acquisition pipeline. You could stream and store on AWS and not have to worry about running anything locally. 

To install mongoDB on Ubuntu, follow the [directions](http://docs.mongodb.org/manual/tutorial/install-mongodb-on-ubuntu/) in the manual:  
(note the following instructions are for Ubuntu version 16.04)

```bash
sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
echo "deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list

sudo apt-get update
sudo apt-get install -y mongodb-org
```

This will install mongoDB. You can check:

```bash
ps awx | grep mongo
```

On Ubuntu, servers are started and stopped mostly with [upstart](http://upstart.ubuntu.com/). Lets start ours:

```bash
sudo service mongod status
sudo service mongod stop
sudo service mongod start
```

### mongoDB on Local

Install mongo locally with brew:    
```
brew update    
brew install mongodb
```
After downloading mongo, we want to create a place for mongo data files to live.  Run:    
```
sudo mkdir -p /data/db
```
Make sure that /data/db directory has the right permissions:

```
sudo chown `active_username` /data/db
(enter password) 
```

(username ~ is just mac username (you can double
check this by running 'whoami' in the terminal)


Run mongo daemon:
```
mongod
```

(In order to access direct mongo functionality, you can just
run 'mongo' in a separate terminal)

Once we're running mongo, we can create, update, delete, etc. databases and interact with ones we already have.

```
help
show dbs
use new_cool_db
show dbs
```

mongoDB is lazy about making things, which is usually a good thing.

```
j = { name: "Eddie" };
k = { name: "Felicity" };
l = { nationality: "British" };
db.testData.insert(j);
db.testData.insert(k);
db.testData.insert(l);
show dbs
show collections
```

Very JavaScript.

```
db.testData.find();
td = db.testData;
td.find();
```

`find` returns a cursor:

```
var c = td.find();
while ( c.hasNext() ) { printjson( c.next() ) }
```

You can search for things!

```
td.find( {x: { $lt: 20 } } );
td.find( {name: { $lt: 'F' } } );
```

Let's put more things in mongo:

```
for (var i=1; i<=25; i++) {
    td.insert( {x : i } );
}
td.find();
it  // iterate
```

Now we can do some more interesting [queries](http://docs.mongodb.org/manual/tutorial/query-documents/):

```
td.find( {x: {$lt : 20 } } );
td.find({$or: [
               { name: "Eddie"},
               {x: { $gt : 22 } }
              ]
});
```

Now, with Python! If you don't have `pymongo` installed, you can `pip install pymongo`. Let's just run a python shell for now to make things fast.

```python
from pymongo import MongoClient

client = MongoClient()
db = client.my_cool_database

db.collection_names()
col = db.my_cool_collection

```

Trying out the data from the 14th challenge:
(we've already copied the challenge data over to the current working directory)

```
unzip heavy_metal_parsed.pkl.zip
```

Back to python:  
```python
from pymongo import MongoClient
client = MongoClient()

import pickle
with open('heavy_metal_parsed.pkl', 'rb') as infile:
    reviews = pickle.load(infile)
reviews[0].keys()
reviews[0]
len(reviews)

hmm = client.my_cool_db.hmm
hmm.insert(reviews[0])
hmm.find().next()

for review in reviews[1:]:
    hmm.save(review)

#some basic exploration:
# lets see what one document looks like:
hmm.find_one()
hmm.count()      
```

Let's work on a version of Challenge #1:   
Make a list of the years in the heavy metal data.  How many heavy metal films came out in 1980?

```python
all_years = []
for film in hmm.find({}, {"year": 1, "_id": 0}):
    all_years.append(film["year"])
    
eighty=[]
for film in hmm.find({"year":1980}, {"year": 1, "_id": 0}):
    eighty.append(film["year"])
    
len(eighty)
```
Using the aggregate function: let's get year frequency:

```
cursor = hmm.aggregate([
    {"$group": {
        "_id": "$year",
        "year_count": {"$sum": 1} 
    }}
])

years = []
counts = []
for doc in cursor:
    years.append(doc["_id"])
    counts.append(doc["year_count"])
```

