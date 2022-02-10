import pickle as pk
import numpy as np
import pandas as pd
from flask import Flask, request, render_template

# Flask constructor
application = Flask(__name__)
@application.route('/')
def home():
      return render_template("index.html")

# A decorator used to tell the application
# which URL is associated function
# prediction function


filename = 'finalized_prediction_model.pk'
loaded_model = pk.load(open(filename, 'rb'))


@application.route('/result', methods=['POST'])
def result():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        TNpeptides  = float(request.form.get("T.N.peptides"))
        TNAlleles = float(request.form.get("T.N Alleles"))
        # getting input with name = lname in HTML form
        NCTs   = float(request.form.get("N.CTs"))
        NcLRPs = float(request.form.get("N.cLRPs"))
        TPHBR = float(request.form.get("TPHBR"))
        TAHBR = float(request.form.get("TAHBR"))
        CombinedStabilityRank = float(request.form.get("Combined Stability Rank"))
        PAS  = float(request.form.get("PAS"))
        

        predictionresult = loaded_model.predict(
            [[TNpeptides, TNAlleles, NCTs , NcLRPs,TPHBR, TAHBR, CombinedStabilityRank, PAS]])
        if int(predictionresult) == 1:
            predictionresult = ' Not eligible for therapy'
        else:
            predictionresult = '  eligible for therapy'

    return render_template("result.html", prediction=predictionresult)

if __name__ == '__main__':
    application.run(debug=True)
    application.config["TEMPLATES_AUTO_RELOAD"]=True
