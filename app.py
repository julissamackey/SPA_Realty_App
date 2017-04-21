from flask import render_template, request, jsonify
from config import db, app
from model import *
import json

@app.route('/<token>', methods = ['GET'])
def start():
	pass

if __name__ == "__main__":
    app.run(debug=True, port=500)
