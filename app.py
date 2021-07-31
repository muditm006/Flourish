from flask import Flask, redirect, url_for, render_template

# redirect - redirects user from pages they aren't supposed to be in
# url_for - gives the app route for the function that is being inputted
# render_template- shows the HTML webpage 

from main import diversity, equity, inclusion, diversity_print, equity_print, inclusion_print

# The main.py file is referenced here and the functions in that file are imported here.

app = Flask(__name__)

# This is the default app route, and where the user goes when they first open the page.
@app.route("/") 
def home():
    return render_template('website.html')


@app.route("/diversity")
def run_diversity():

    # The 'diversity()' function is what produces the graphs.
    diversity("sample_dataset.csv")
    
    # The 'diversity_print()' function is what produces the written summary for the user.
    a= diversity_print("sample_dataset.csv")
    
    return a

@app.route("/equity")
def run_equity():

    # The 'equity()' function is what produces the graphs.
    equity("sample_dataset.csv")
    
    # The 'equity_print()' function is what produces the written summary for the user.
    b= equity_print("sample_dataset.csv")
    
    return b

    
@app.route("/inclusion")
def run_inclusion():

    # The 'inclusion()' function is what produces the graphs.
    inclusion("sample_dataset.csv")
    
    # The 'inclusion_print()' function is what produces the written summary for the user.
    c = inclusion_print("sample_dataset.csv")
    
    return c


if __name__ == "__main__":
    app.run()
