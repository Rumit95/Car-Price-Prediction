from flask import Flask,render_template,request
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OrdinalEncoder

app = Flask(__name__)
app.secret_key="abc"

def encode(wheel_d,engine_l):
    enc = pickle.load(open('encode.pkl','rb'))
    x1=enc.fit_transform([[wheel_d,engine_l]])
    return x1

def pred(list1):
    model = pickle.load(open('predict.pkl','rb'))
    price=model.predict([list1])[0]
    return price

@app.route("/")
def home():
    return render_template ('Home.html')

@app.route("/pred",methods=["POST"])
def check_fun():
    wheel_drive=request.form["wheel_drive"]
    engine_location=request.form["engine_location"]
    width=float(request.form["width"])
    engine_size=float(request.form["engine_size"])
    horsepower=float(request.form["horsepower"])
    city_mpg=float(request.form["city_mpg"])
    highway_mpg=float(request.form["highway_mpg"])
    x=encode(wheel_drive,engine_location)
    l1=[x[0][0],x[0][1],width,engine_size,horsepower,city_mpg,highway_mpg]
    p=pred(l1)
    return render_template("Home.html",price=round(p,2))

if __name__ =='__main__':
    app.run(debug=True)