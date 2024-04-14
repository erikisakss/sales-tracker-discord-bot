from flask import Flask
import requests

app = Flask(__name__)

@app.route('/<name>')

def apicall(name):
    url = 'https://api.steampowered.com/ISteamApps/GetAppList/v2/'
    response = requests.get(url)
    data = response.json()

    matching_apps = [app for app in data['applist']['apps'] if app['name'].lower() == name.lower()]
    return {'matching_apps': matching_apps}