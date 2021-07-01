from flask import Flask, render_template, request
import csv
from hlsPD import HLSpd
import werkzeug
# from hlsTF import HLStf

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '.'
app.config['MAX_CONTENT_PATH'] = 1024*1024*25

@app.route('/' , methods=['GET','POST'])
@app.route('/upload' , methods=['GET','POST'])
def upload():
    return render_template('upload.html')

@app.route('/data', methods=['GET','POST'])
def data():
    if request.method == 'POST':
        f = request.files['file']
        hls = HLSpd(f)
        numericStats = hls.print_stats_numeric()
        catStats =  hls.print_stats_numeric()
        return render_template('data.html', data= [numericStats, catStats]) #tfdvStats

if __name__ == '__main__':
    app.run(debug=True)
