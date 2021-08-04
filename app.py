from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('app.html')

@app.route('/answer',methods = ['POST','GET'])
def solution():
    a = float(request.form['A-value'])
    b = float(request.form['B-value'])
    c = float(request.form['C-value'])
    d = float(request.form['D-value'])

    sludge_volume = 109.91379 - (0.001717 * a) - (0.000237 * b) + (4.05308 * c) - (17.12600 * d) 
    + (0.000000017472 * a * b) - (0.000125 * a * c) + (0.003618 * a * d) - (0.00000236838 * b * c)
    + (0.000261 * b * d) - (4.28208 * c * d) - (0.000000714638 * a * a) - (0.00000000081293 * b * b)
    + (0.095687 * c * c) + (4.29643 * d * d)

    sludge_volume = round(sludge_volume,2)
    return "Sludge volume: "+str(sludge_volume)

if __name__=="__main__":
    app.run(debug=True)

