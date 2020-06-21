from flask import Flask, render_template, current_app
import os,sys
from dotenv import load_dotenv
import tda
import atexit

app = Flask(__name__)

def make_webdriver():
    from selenium import webdriver
    from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
    
    browser = webdriver.Chrome()
    atexit.register(lambda: browser.quit())
    return browser

@app.route("/")
def hello():
    tda.auth.easy_client(current_app.config["TDAMERITRADE_CLIENT_ID"], current_app.config["REDIRECT_URI"], current_app.config["PATH_TO_TOKEN"], make_webdriver)
    return render_template("whale_hello.html")

if __name__ == '__main__':
    project_folder = os.path.dirname(os.path.abspath(__file__))
    load_dotenv(os.path.join(project_folder, '.env'))
    authtoken_path = os.path.join(project_folder, 'authtoken.txt')
    app.config.update(
    TDAMERITRADE_CLIENT_ID=os.getenv("TDAMERITRADE_CLIENT_ID"),
    REDIRECT_URI=os.getenv("REDIRECT_URI"),
    PATH_TO_TOKEN=authtoken_path
    )
    app.run(debug=True, host='0.0.0.0', port='5000', ssl_context='adhoc')