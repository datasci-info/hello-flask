from flask import Flask
from flask import request
app = Flask(__name__)

@app.route("/")
def hello():
  print request
  # print dir(request)

  print "request.path", request.path
  print "request.method", request.method
  print "request.user_agent", request.user_agent
  print "request.query_string", request.query_string
  print "request.cookies", request.cookies
  print "request.args", request.args
  print "request.form", request.form

  return "<hr>".join(map(lambda key:"request."+key+" = " + str(request.__dict__[key]),request.__dict__.keys()))


if __name__ == "__main__":
    app.run()