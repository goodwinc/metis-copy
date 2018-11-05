import flask
import numpy as np
import pandas as pd
from copy import deepcopy

# Initialize the app
app = flask.Flask(__name__)

@app.route("/")
def viz_page():
    with open("pair_solution2.html", 'r') as viz_file:
        return viz_file.read()

@app.route("/gof", methods=["POST"])
def score():
    """
    When A POST request with json data is made to this url,
    Read the grid from the json, update and send it back
    """
    data = flask.request.json
    a = data['grid']
    n = int(len(a)**0.5)
    change = 0
    b = a[:]
    for i in range(1,n-1):
        for j in range(1,n-1):
            count=b[(i-1)*n+j]+b[(i+1)*n+j]+b[(i-1)*n+j-1]+b[(i+1)*n+j-1]+b[(i-1)*n+j+1]+b[(i+1)*n+j+1]+b[i*n+j-1]+b[i*n+j+1]
            if b[i*n+j]:
                if count<2 or count>3:
                    a[i*n+j]=0
                    change=1
            else:
                if count==3:
                    a[i*n+j]=1
                    change=1
    return flask.jsonify({'grid': a, 'change': change})

#--------- RUN WEB APP SERVER ------------#

# Start the app server on port 80
# (The default website port)
app.run(host='0.0.0.0', port=5000)
