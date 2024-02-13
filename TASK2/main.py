from flask import Flask, request,Response ,jsonify;
import json

from werkzeug.exceptions import HTTPException

app = Flask(__name__)

#handle bad requests
@app.errorhandler(HTTPException)
def handle_bad_request(e):
    return 'Invalid input.', 400

#create a POST endpoint
@app.route("/api", methods = ['POST'])
def identifyUnauthorizedSales():
    #list that will containt the unauthorized sales
    unauthorizedSales = []
    #fetch sent data
    receivedData = json.loads(request.data);
    #go through all sale transactions and double check their sellerId with the authorized ones
    for salesTransaction in receivedData["salesTransactions"]:
        for productListing in receivedData["productListings"]:
            if((productListing["productID"] == salesTransaction["productID"]) and (productListing["authorizedSellerID"] != salesTransaction["sellerID"])):
                unauthorizedSales.append(salesTransaction)
    #create a response in the given format
    response = {"unAuthorizedSales" : unauthorizedSales}
    
    if(len(unauthorizedSales) != 0):
        return jsonify(response), 201
    #return 204 if the request was succesfull but no sales were found
    else:
        return Response(status=204)

        
