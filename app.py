from flask import Flask, render_template, request
import csv
from hlsPD import HLSpd
from hlsTF import HLStf

app = Flask(__name__)

@app.route('/' , methods=['GET','POST'])
def pd():
    return render_template('index.html')

@app.route('/data', methods=['GET','POST'])
def data():
    if request.method == 'POST':
        f = request.form['csvfile']
        # print(f)
        # print(type(f))
        # data = []
        # with open(f) as file:
        #     csvfile = csv.reader(file)
        numericStats = HLSpd(f).print_stats_numeric()
        catStats =  HLSpd(f).print_stats_numeric()

        tfdvStats = HLStf(f).generate_HLstats_json()

        return render_template('data.html', data= [numericStats, catStats, tfdvStats])




@app.route('/tfdv')
def tfdv():
    pass

if __name__ == '__main__':
    app.run(debug=True)
