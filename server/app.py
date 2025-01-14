from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:parameter>')
def print_string(parameter):
    print(parameter)  
    return parameter  

@app.route('/count/<int:parameter>')
def count(parameter):
    numbers = '\n'.join(str(i) for i in range(parameter)) + '\n'
    return numbers  

@app.route('/math/<int:num1>/<string:operation>/<int:num2>')
def math(num1, operation, num2):
    """
    Performs the specified operation (+, -, *, div, %) on two numbers.
    """
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '%':
            result = num1 % num2
        elif operation == 'div':
            if num2 == 0:
                return "Error: Division by zero is not allowed.", 400
            result = num1 / num2
        else:
            return "Error: Unsupported operation.", 400

        return str(result) 
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(port=5555, debug=True)
