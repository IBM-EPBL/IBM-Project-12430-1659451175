from flask import Flask,render_template, url_for

app=Flask(__name__)

@app.route('/')
@app.route('/web detection.html')
def Home():
           return render_template("web detection.html")
    
@app.route('/')
@app.route('/About.html')

def About():
       return render_template("About.html")
     
if __name__ == "__main__":   
 app.run(debug=True)
    