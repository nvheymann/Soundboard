import flask
#from playsound import playsound
import os
from flask import request, jsonify

app = flask.Flask(__name__)



# A route to return all of the available entries in our catalog.
@app.route('/api/play/<sound>', methods=['GET'])
def api_all(sound):
    os.system('mpg123 /sounds/' + sound)
    #playsound("/var/www/html/"+sound)
    return jsonify({'statuscode': '200'})


app.run(host='0.0.0.0')
