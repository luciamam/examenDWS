from  flask import Flask, render_template, url_for, flash


app=Flask(__name__)





@app.route('/')
def inicio():
    return " soy la ruta raiz  "




@app.route('/registrarse', methods=['GET','POST'])
def registro():
    return " soy la ruta registro "




if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0')