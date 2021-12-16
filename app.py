import csv
from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__, static_url_path='/static')


@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html', title='Index')

@app.route('/Pylindt_and_Others')
def Pylindt_and_Others():
    return render_template('Article1PylintandOthers.html', title='Pylint and others')

@app.route('/AAA_Testing')
def AAA_Testing():
    return render_template('Article2AAATesting.html', title='AAA Testing')

@app.route('/OOP')
def OOP():
    return render_template('Article3OOP.html', title='OOP')

@app.route('/Article4')
def Article_4():
    return render_template('Article4.html', title='Article 4')

@app.route('/aboutpage')
def About():
    return render_template('about.html', title='About')

@app.route('/Calculator_page')
def Calculator_page():
    return render_template('calculator_page.html', title='Calculator')


@app.route('/calculation_history')
def calculation_history():
    records = []
    with open('F:\FL Flask\Sehrish Calculator\CalculatorHistory\MyCalculations.csv') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if len(row) < 1:
                break
            records.append(row)
        data = {
            'records': records,
        }
        return render_template('history_calc.html', data=data)

@app.route('/calculate_data', methods=['POST'])
def Calculate_Data():
    result = 0
    try:
        operator = request.form['btnradio']
        value1 = int(request.form['value1'])
        value2 = int(request.form['value2'])
        if operator == 'division':
            result = value1/value2
        elif operator == 'multiplication':
            result = value1 * value2
        elif operator == 'addition':
            result = value1 + value2
        elif operator == 'subtraction':
            result = value1 - value2

        data = {
            'value':result,
        }
        data_file = open('F:\FL Flask\Sehrish Calculator\CalculatorHistory\MyCalculations.csv', mode='a', newline='')
        writer = csv.writer(data_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([datetime.now().strftime('%d-%m-%Y %H:%M'), value1, value2, operator, result])
        data_file.close()
        return render_template('calc_output.html', data=data)
    except Exception as e:
        data = {
            'value':str(e)
        }
        return render_template('calc_output.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
