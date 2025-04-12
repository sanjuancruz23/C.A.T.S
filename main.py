# Import needed modules from flask
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def index():
