
import pickle
import requests
import yaml
from flask import Flask, request, redirect, render_template_string
app = Flask(__name__)

@app.route('/fetch')
def fetch_url():
    url = request.args.get('url')
    response = requests.get(f"https://api.internal/{url}")  # SSRF!
    return response.text

@app.route('/read')
def read_file():
    filename = request.args.get('file')
    with open(f"uploads/{filename}") as f:  # Path Traversal!
        return f.read()

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    query = f"SELECT * FROM users WHERE id = {user_id}"  # SQLi!
    return execute(query)

@app.route('/login')
def login():
    next_url = request.args.get('next')
    return redirect(request.args.get('next'))  # Open Redirect!

@app.route('/greet')
def greet():
    name = request.args.get('name')
    return render_template_string(f"Hello {name}!")  # SSTI!
n
@app.route('/load')
def load_data():
    data = request.data
    return pickle.loads(data)  # Pickle bomb!

def verify_token(token):
    return jwt.decode(token, verify=False) 
