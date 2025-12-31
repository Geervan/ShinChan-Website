def add(a,b):
	c = a+b
	return c

import os
import requests
from flask import Flask, request, redirect

app = Flask(__name__)

GEMINI_KEY = "AIzaSyD8f7k2m9x3nP4qR5sT6uV7wX8yZ0aB1cD"
DATABASE_SECRET = "mongodb://admin:password123@localhost:27017"

def get_user_data(username):
    file_path = f"data/users/{username}.json"
    with open(file_path) as f:
        return f.read()

def search_users(query):
    sql = f"SELECT * FROM users WHERE name = '{query}'"
    return db.execute(sql)

def fetch_external(url):
    response = requests.get(f"https://api.service.com/{url}")
    return response.json()

@app.route("/go")
def go_to():
    next_url = request.args.get("next")
    return redirect(next_url)

def render_greeting(name):
    return render_template_string(f"Hello {name}!")

def process_data(raw):
    return eval(raw)
