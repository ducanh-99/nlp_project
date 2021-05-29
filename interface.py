# import sys
# sys.path.append('D:/Tai Lieu/HUST-Study/20202/NLP/project/code')

from flask import Flask, request, render_template

from url_input import get_url, get_information


from NLP import findAll

app = Flask(__name__)
 
@app.route('/')
def my_form():
    return render_template('homepage.html')

@app.route('/', methods=['POST'])
def information():
    url = request.form['text']
    soup = get_url(url)
    infor = get_information(soup=soup)
    typeE, cateE, ae, road, dt, ct, pr, number, fullname = findAll(infor) 
    return render_template('homepage.html', output=infor, input=url,typeE = ', '.join(typeE),\
                                            cateE = ', '.join(cateE),ae=', '.join(ae),road=', '.join(road),\
                                            dt=', '.join(dt),ct =', '.join(ct), pr=', '.join(pr),\
                                            number=', '.join(str(i) for i in number), fullname=', '.join(fullname))

if __name__ == '__main__':
    app.run(debug=True)