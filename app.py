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


@app.route('/level-4')
def level_4():
    return render_template('level-4.html')

@app.route('/level-5')
def level_5():
    return render_template('level-5.html')

@app.route('/level-6')
def level_6():
    return render_template('level-6.html', level=6)

@app.route('/level-7')
def level_7():
    return render_template('level-7.html')

if __name__ == '__main__':
    app.run(debug=True)
