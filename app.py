from flask import Flask, render_template

app = Flask(__name__, template_folder='src')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/levels')
def levels():
    return render_template('levels.html')

@app.route('/level-1')
def level_1():
    return render_template('level-1.html')

@app.route('/level-2')
def level_2():
    return render_template('level-2.html')

@app.route('/level-3')
def level_3():
    return render_template('level-3.html')

if __name__ == '__main__':
    app.run(debug=True)
