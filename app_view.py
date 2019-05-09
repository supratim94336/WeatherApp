import os, re
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS


app = Flask(__name__)
api = Api(app)
CORS(app)


# class which inherits REST API model
class WeatherAppAPI(Resource):
    def post(self):
        """
        get_json(force=False, silent=False, cache=True)¶
        Parse and return the data as JSON. If the mimetype does not indicate JSON (application/json, see is_json()),
        this returns None unless force is true. If parsing fails, on_json_loading_failed() is called and its return
        value is used as the return value.
        :return:
        """
        json_data = request.get_json()
        latitude = json_data['latitude']
        longitude = json_data['longitude']
        start_date = json_data['start_date']
        end_date = json_data['end_date']


api.add_resource(WeatherAppAPI, '/weather')
if __name__ == '__main__':
    app.run(debug=False)
