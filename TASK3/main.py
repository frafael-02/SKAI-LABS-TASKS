from operator import itemgetter
from flask import Flask, request,Response ,jsonify;
import json

from werkzeug.exceptions import HTTPException

app = Flask(__name__)

#handling bad requests
@app.errorhandler(HTTPException)
def handle_bad_request(e):
    return 'Invalid input.', 400

#create a POST endpoint
@app.route("/api", methods = ['POST'])
def identifyUnauthorizedSales():
    interviews = []
    results = []
    index = 0;
    #fetching data from the request and saving it into an array of interview dicts
    receivedData = json.loads(request.data);
    for i in range (len(receivedData['start_times'])):
        interviews.append({'start_time' : receivedData['start_times'][i],
                           'end_time' : receivedData['end_times'][i]})
        
    #sort interviews by starting times
    interviews.sort(key=itemgetter('start_time'))

  #get max interviews possibility for each interview set as a starting point
    for y in range (len(receivedData['start_times'])-1):
        results.append(0)
        index = y
        for i in range (len(receivedData['start_times'])-1):
            if(interviews[index]['end_time'] <= interviews[i+1]['start_time']):
                results[y] = results[y] + 1
                index=index+1

            
    #sending a response and adding 1 for the starting interview
    response = {
        "max_interviews" : max(results)+1
    }
    return jsonify(response), 200

        
