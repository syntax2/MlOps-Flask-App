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

#variable rule
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score>=50:
        res="pass"
    else:
        res="FAIL"
    return render_template('result.html',results=res)

@app.route('/form', methods=['GET', 'POST'])
def form():
    result = None
    if request.method == 'POST':
        # Get form data
        input_text = request.form.get('input_text')
        numeric_param = request.form.get('numeric_param')
        
        # Process the input (you can add your ML model processing here)
        result = f"Received text: {input_text}, numeric parameter: {numeric_param}"
        
        # Pass the result back to the template
        return render_template('form.html', result=result)
    
    # If it's a GET request, just show the empty form
    return render_template('form.html')


# This should always come last - it starts your server
if __name__=="__main__":
    # Adding debug=True helps during development
    app.run(debug=True)

