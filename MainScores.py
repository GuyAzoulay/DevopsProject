
from Utils import *
from flask import Flask, render_template
from Live import *
app = Flask(__name__,template_folder='templates')


def score_server():
    screen_cleaner()
    load_game()
    with open(SCORE_FILE_NAME, "r") as score_file:
        global scr
        scr = score_file.read()
    if scr == "":
        @app.route("/lost", methods=['POST', 'GET'])
        def lost():
            return render_template('lost.html', BADSCORE=BAD_RETURN_CODE)
    else:
        @app.route("/win", methods=['POST', 'GET'])
        def lost():
            return render_template('win.html', SCORE=scr)


@app.route("/")
def index():
    return render_template('index.html')









if __name__ == '__main__':
    score_server()
    app.run(port=9999)