
from flask import Flask, render_template, request

import pickle
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')



@app.route('/predict',methods=['POST'])
def predict():

    if request.method == 'POST':

        spl = request.form['spl']
        spw = request.form['spw']
        ptl = request.form['ptl']
        ptw = request.form['ptw']

        data =[[float(spl),float(spw),float(ptl),float(ptw)]]

        lr = pickle.load(open('iris.pkl', 'rb'))
        prediction = lr.predict(data)[0]

    return render_template('index.html', prediction=prediction)



if __name__ == '__main__':
    app.run()

































































































'''

from flask import Flask,render_template,request
import pickle 
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():

    lr = pickle.load(open('iris.pkl','rb'))

    if request.method =='POST':
        sepelL = request.form['spl']
        sepelW = request.form['spw']
        petalL = request.form['ptl']
        petalW = request.form['ptw']

        data = [[int(sepelL),int(sepelW),int(petalL),int(petalW)]]

        prediction = lr.predict(data)[0]

        
    return render_template('index.html',prediction=prediction)

if __name__ == '__main__':
    app.run()





    <form action="/predict" method="POST">

        <input type="text" name="spl" placeholder="Enter Petal Length">
        <input type="text" name="spw" placeholder="Enter Petal Width">
        <input type="text" name="ptl" placeholder="Enter Sepel Length">
        <input type="text" name="ptw" placeholder="Enter Sepel Length">

        <button class="btn btn-primary">Predict</button>


    </form>


    
    {% if prediction %}

    <h1>{{prediction}}</h1>
        
    {% endif %}
        



'''