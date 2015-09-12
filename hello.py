from flask import Flask, send_from_directory
import os

app = Flask(__name__, static_url_path=os.path.join(os.getcwd(),"static"))

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/js/<path:path>')
def send_js(path):
  return send_from_directory('static/js/', path)


if __name__ == "__main__":
  app.debug = True
  app.run()