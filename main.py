from flask import Flask, render_template
from revApiCall import revSpeechmod
import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print
        'test.py -i <inputfile> -o <outputfile>'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print
            'test.py -i <inputfile> -o <outputfile>'
            sys.exit()
        elif opt in ("-i", "--ifile"):
            if("json" in arg):
                revSpeech = revSpeechmod(arg)
            elif("mp3" in arg):
                revSpeech = revSpeechmod()
                revSpeech.getTranscript(arg)
            else:
                print("Error")
                break
    revSpeech.setSwears('swears.json')
    num, swears = revSpeech.checkSwears()
    app.run(debug=True)


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
    main(sys.argv[1:])
