from flask import Flask, redirect, url_for, request,render_template
import pickle
import numpy as np
import sklearn
app = Flask(__name__)
  

def ValuePredictor(to_predict_list):
    to_predict = np.array(to_predict_list).reshape(1,2)
    loaded_model = pickle.load(open("kmeanscluster.pkl", "rb"))
    result = loaded_model.predict(to_predict)
    return result


@app.route("/")
def index():
    return render_template("index.html"); 
@app.route('/result',  methods =["GET", "POST"])
def result():
    if request.method == "POST":
       
       age = request.form.get("age")
       estimated_salary= request.form.get("estimated_salary")
       l1=[age,estimated_salary]
       answer = ValuePredictor(l1)
    return render_template("result.html",Age=answer)
   
  
if __name__ == '__main__':
   app.run(debug = True)