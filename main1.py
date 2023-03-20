from flask import Flask,render_template,request
import pickle

# This is create an instance for Flask class

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("homepage.html")

@app.route('/homepage',methods=['POST','GET'])  # route to display the home page
def homepage():
    if request.method == 'POST':
        try:
            hours = float(request.form.get('hours'))
            model2 = pickle.load(open("demo.pkl","rb"))
            prediction = model2.predict([[hours]])[0]
            print("Prediction value: ",prediction)
            return render_template('result.html', prediction=prediction)
        except Exception as e:
            return "Something went wrong"
    else:
        return render_template('homepage.html')


if __name__ == '__main__':
    app.run(debug=True)
