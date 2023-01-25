from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        age = float(request.form['age'])
        sex = float(request.form['sex'])
        cp = float(request.form['cp'])
        trestbps = float(request.form['trestbps'])
        chol = float(request.form['chol'])
        fbs= float(request.form['fbs'])
        restecg = float(request.form['restecg'])
        thalach = float(request.form['thalach'])
        exang = float(request.form['exang'])
        oldpeak = float(request.form['oldpeak'])
        slope = float(request.form['slope'])
        ca = float(request.form['ca'])
        thal = float(request.form['thal'])

        pred_args = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]

        mul_reg = open('heart_model.pkl','rb')
        ml_model = joblib.load(mul_reg)
        model_predcition = ml_model.predict([pred_args])
        if model_predcition == 1:
            res = 'Sorry you have chances of getting the disease. Please consult the doctor immediately'
        else:
            res = 'No need to fear. You have no dangerous symptoms of the disease'
        #return res
    return render_template('result.html', prediction_text = res)

if __name__ == '__main__':
    app.run(debug=True)
