from asyncio.log import logger
import os
import re
import json
# import nltk
import difflib
import urllib
import pickle
import numpy as np
import pandas as pd
import logging
from pathlib import Path
from bs4 import BeautifulSoup

from flask import Flask, app, request
from flask_cors import CORS, cross_origin

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
import pickle
from script_logger import App_Logger


# model = pickle.load(open("./api_utils/RFR-sales-02-06-2022-09-19-20.pkl", "rb"))
# scaler = pickle.load(open("./api_utils/scaler-02-06-2022-09-19-20.pkl", "rb"))

app = Flask(__name__)

cors = CORS(app)


@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add(
        "Access-Control-Allow-Headers", "Origin, X-Requested-With, Content-Type, Accept"
    )
    response.headers.add("Access-Control-Allow-Methods",
                         "GET,PUT,POST,DELETE,OPTIONS")
    response.headers.add("Access-Control-Allow-Credentials", "true")
    return response


def convert(o):
    if isinstance(o, np.generic):
        return o.item()
    raise TypeError



@app.route("/get_file", methods=["POST", "GET"])
def file_getter():
    loggerr=App_Logger("script.log").get_app_logger()
    if request.method == "POST":
        try:
            file = request.files["file"]
            print(file)
            loggerr.info(file.filename)
            # loggerr.info(f"FIle Type: {file.mimetype}")
            # print()
            return json.dumps({"success": "File Uploaded Successfully"}, default=convert)
            # print(submitted_file)
        except Exception as e:
            print(e)
            return json.dumps({"error": "Couldn't handle uploaded file. "}, default=convert)
    else:
        print("error")
        return json.dumps({"error": "No POST Data"}, default=convert)
    
    
    
    

@app.route("/", methods=["POST", "GET"])
def home():
    return json.dumps({"result": "This is Movie Recommender API"}, default=convert)



if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
