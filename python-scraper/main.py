from flask import Flask
import requests

app = Flask(__name__)

@app.route('/<name>')

def apicall(name):
    url = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'
    response = requests.get(url)
    return response.json()