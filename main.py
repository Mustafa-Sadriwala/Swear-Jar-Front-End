from flask import Flask, render_template
from revApiCall import revSpeechmod

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/swears")
def swears():
    return render_template("swears.html")

if __name__ == "__main__":
    revSpeech = revSpeechmod('audio.mp3.json')
    #revSpeech.getTranscript('audio.mp3')
    revSpeech.checkSwears()
    app.run(debug=True)
