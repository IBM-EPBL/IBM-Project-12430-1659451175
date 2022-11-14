

import flask
from flask import request, render_template
from flask_cors import CORS
import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "2ev1GR8SAtWLwWssYOE18Lsh2PnIrqX2baPc6kSY84cf"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey":
 API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

app=Flask(__name__)

@app.route('/')
@app.route('/web.html')
def Home():
           return render_template("web.html")
    
@app.route('/')
@app.route('/About.html')

def About():
       return render_template("About.html")


    # NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"fields": [array_of_input_fields], "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/2de01c97-1fd7-44b5-aec3-f15bb3d28d2e/predictions?version=2022-11-10', json=payload_scoring,
 headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())
  # showing the prediction results in a UI# showing the prediction results in a UI 
pred=print(predictions['predictions'][0]['values'][0][0])
if(pred != 1):
    print("The Website is secure. you are safe....")
else:
    print("The Website is not Legitimate !!BEWARE!!")
    
    

if __name__ == "__main__":
    app.run(debug=True,port=5500)