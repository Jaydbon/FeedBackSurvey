from flask import Flask, render_template, redirect, url_for
import json

app = Flask(__name__)
questions = questions = [
    (1, "Rate the experience", "slider"),
    (2, "What did you not like about it?", "text"),
    (3, "How easy was it to navigate the website?", "slider"),
    (4, "What did you like most about the website?", "text"),
    (5, "How visually appealing did you find the design?", "slider"),
    (6, "What could we improve to make your experience better?", "text"),
    (7, "How satisfied are you with the website’s loading speed?", "slider"),
    (8, "Did you encounter any issues or bugs while using the site?", "text"),
    (9, "How likely are you to return to this website in the future?", "slider"),
    (10, "Is there any feature or content you wish the website had?", "text")
]


x=0



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/survey')
def survey():
    if questions[x][2] == "slider":
        return render_template('slider.html', question=questions[x])
    else:
        return render_template('textbox.html', question=questions[x])
    
@app.route('/previous')
def previous():
    global x
    x = x - 1
    print(questions[x])
    return redirect(url_for('survey'))

@app.route('/next', methods=["POST"])
def next():
    global x
    x = x + 1
    answer = request.form.get('response')


    return redirect(url_for('survey'))


if __name__ == '__main__':
    app.run(debug=True)