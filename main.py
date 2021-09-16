from flask import Flask, jsonify
from threading import Thread
from flask_restful import Resource, Api
#from flask_swagger_ui import get_swaggerui_blueprint
import json
import random


app = Flask('')
api = Api(app)


@app.route('/')
def home():
  return "I'm alive"


#################################
##API USING FLASK-RESTFUL

class Test(Resource):
  def get(self):
    return jsonify({"Type": "flask-restful"})


def get_orders(order_type):
  if order_type == "arrival":
    file_address = 'Orders/curbside.json'
  else:
    file_address = 'errormsg.json'  
  with open(file_address, 'r') as orderfile:
    data = json.load(orderfile)
  order = random.choice(list(data['Orders']))

  return order 


class Orders(Resource):
  def get(self, order_type):
    return get_orders(order_type)

api.add_resource(Orders, '/curbside/<string:order_type>')

def run():
  app.run(host='0.0.0.0',port=7210)

  
t = Thread(target=run)
t.start()



