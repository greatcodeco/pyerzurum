from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'linuxdegilgnulinux'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/participation')
def participation():
    return render_template('katilim.html')

@app.route('/about')
def about():
    return render_template('hakkinda.html')

@app.route('/contact')
def contact():
    return render_template('iletisim.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
