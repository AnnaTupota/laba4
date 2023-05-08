from flask import Flask, render_template, request
import math
app = Flask(__name__)#обьект передаем название файла
#основной файл main
@app.route('/')
def form1():
    return render_template('1.html')

@app.route('/2.html', methods=['post', 'get'])#КОНУС
def form2():
    num_1=0;
    num_2=0;
    num_3=0;
    if request.method == 'POST':
        num_1 = float(request.form.get('num_1'))
        num_2 = float(request.form.get('num_2'))
        num_3 = int(request.form.get('num_3'))
    b1 = round(((1 / 3) * (num_1 ** 2) * math.fabs(num_2)), abs(num_3))
    print(b1)
    return render_template('2.html', ans1=b1)

@app.route('/3.html', methods=['post', 'get'])
def form3():#ШАР
    num_4 = 0;
    num_5 = 0;

    if request.method == 'POST':

        num_4 = float(request.form.get('num_4'))
        num_5 = int(request.form.get('num_5'))
    b2 = round(((4 / 3) * math.fabs(num_4 ** 3)*math.pi ), abs(num_5))
    print(b2)
    return render_template('3.html', ans2=b2)

@app.route('/4.html', methods=['post', 'get'])#ПИРАМИДА
def form4():
    num_6 = 0;
    num_7 = 0;
    num_8 = 0;
    if request.method == 'POST':

        num_6 = float(request.form.get('num_6'))
        num_7 = float(request.form.get('num_7'))
        num_8 = int(request.form.get('num_8'))
    b3 = round(((1 / 3) * math.fabs(num_6 * num_7 ) ), abs(num_8))
    print(b3)
    return render_template('4.html', ans3=b3)
@app.route('/5.html', methods=['post', 'get'])
def form5():#УСЕЧЕННАЯ ПИРАМИДА
    num_9 = 0;
    num_10 = 0;
    num_11 = 0;
    num_12=0
    if request.method == 'POST':

        num_9 = float(request.form.get('num_9'))
        num_10 = float(request.form.get('num_10'))
        num_11 = float(request.form.get('num_11'))
        num_12 = int(request.form.get('num_12'))

    b4 = round(((1 / 3) * math.fabs(num_9) * (math.fabs(num_10)+( math.fabs(num_10)+ math.fabs(num_11))**(1/2)+ math.fabs(num_11) ) ), abs(num_12))
    print(b4)
    return render_template('5.html', ans4=b4)
@app.route('/6.html', methods=['post', 'get'])
def form6():#призма
    num_13 = 0;
    num_14 = 0;
    num_15 = 0;
    if request.method == 'POST':

        num_13 = float(request.form.get('num_13'))
        num_14 = float(request.form.get('num_14'))
        num_15= int(request.form.get('num_15'))
    b5 = round(((1 / 3) * math.fabs(num_13 * num_14 ) ),abs(num_15))
    print(b5)
    return render_template('6.html', ans5=b5)

@app.route('/7.html', methods=['post', 'get'])
def form7():#цилиндр
    num_16 = 0;
    num_17 = 0;
    num_18 = 0;
    if request.method == 'POST':

        num_16 = float(request.form.get('num_16'))
        num_17 = float(request.form.get('num_17'))
        num_18= int(request.form.get('num_18'))
    b7 = round(math.fabs(num_16 * (num_17**2)*math.pi) , abs(num_18))
    print(b7)
    return render_template('7.html', ans6=b7)

@app.errorhandler(ValueError)
def pageNotFount(error):
    return render_template('ERORRRR.html')

if __name__ == '__main__':
    app.run()