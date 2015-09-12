from flask import Flask, render_template
app = Flask(__name__)

#TODO: store sample messages into DB
#TODO: read messages from DB
sample_messages = ["Message!", "Hello! Flask!", "Flask is awesome!", "new message"]

@app.route('/')
def guestbook():
  #TODO: read messages from DB
  return render_template('hello.html', messages = sample_messages)

if __name__ == "__main__":
    app.run()