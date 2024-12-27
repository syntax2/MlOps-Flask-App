from flask import Flask,render_template, request

# Create the Flask application instance
app = Flask(__name__)

# Define your routes BEFORE running the application
@app.route('/')
def welcome():
    return "<html><H1>hello world to MLOps, i will make it</H1></html>"

@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method=='POST':
        pass
    return render_template('form.html')

# This should always come last - it starts your server
if __name__=="__main__":
    # Adding debug=True helps during development
    app.run(debug=True)

