from flask import Flask 
import requests
import os
from app import Scrap

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello chandu is here !"    # for testing 

# @app.route('/app', methods=['POST']) # Endpoint/<<type>:arguments >        
# def funtion_name():
#     url = requests.get_json()['url']
#     is_exist = os.path.exists("cookies.pkl")
#     a = Scrap()
    
#     if not(is_exist):
#         a.login()
    
#     res = a.get(url)

#     return {"download_url" : res}


@app.route('/insta/<String:s>')
def funtion_name(n,m):
    result = {"A":321,"B":654,"Sum":95+654,"Server ip":"127.0.0.1:5500"}
    # yours result in python dictionry form
    return  jsonify(result)

if __name__=="__main__":
    app.run(debug=True) 
