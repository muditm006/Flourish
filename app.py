from flask import Flask, redirect, url_for, render_template
import os


# redirect - redirects user from pages they aren't supposed to be in
from main import diversity, equity, inclusion, diversity_print, equity_print, inclusion_print


app = Flask(__name__)



# give route to show Flask the path to get to the function


@app.route("/")  # the / is default url
def home():
    return render_template('website.html')

@app.route("/diversity")
def run_diversity():
    diversity("sample_dataset.csv")
    a= diversity_print("sample_dataset.csv")
    return a

@app.route("/equity")
def run_equity():
    equity("sample_dataset.csv")
    b= equity_print("sample_dataset.csv")
    return b

    

    
@app.route("/inclusion")
def run_inclusion():
    inclusion("sample_dataset.csv")
    c = inclusion_print("sample_dataset.csv")
    return c

 

# @app.route("/<name>")  # can input parameter directly in the URL
# def user(name):
#     return ("Hello " + name + "!")

@app.route("/admin")
def admin():
    return redirect(url_for("home")) # redirect to the function named "home"


if __name__ == "__main__":
    app.run()
