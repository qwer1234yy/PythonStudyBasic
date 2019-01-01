from flask import Flask,render_template
import json
app = Flask(__name__, static_url_path='/js')

@app.route('/')
def index():
    return 'index'

@app.route('/test1')
def test1():
    data = {'cities':['北京', '广州', '深圳', '重庆', '成都', '武汉'],
            'high':[20,21,31,23],
            'avg':[20,21,31,23],
            'low':[20,21,31,23]}
    return json.dumps(data)

@app.route('/test2')
def test2():
    return render_template('highchart_salary_tester_v2.html')


if __name__ == '__main__':
    app.run()