from flask import Flask, render_template
import os
from dotenv import load_dotenv


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("whale_hello.html")

if __name__ == '__main__':
    project_folder = os.path.dirname(os.path.abspath(__file__))
    load_dotenv(os.path.join(project_folder, '.env'))
    TDAMERITRADE_CLIENT_ID = os.getenv("TDAMERITRADE_CLIENT_ID")
    print(TDAMERITRADE_CLIENT_ID)
    app.run(debug=True, host='0.0.0.0')