from flask import Flask, render_template, url_for
from modules import convert_to_dict
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

app = Flask(__name__)
application = app 

#create new secret key
app.config['SECRET_KEY'] = 'C2HWGVoMGfNTBsrYQg8EcMrdTimkZfAb'

Bootstrap(app)

songs_list = convert_to_dict("songs.csv")

@app.route('/')
def index():
    num_list = []
    name_list = []
    # fill one list with the number of each presidency and
    # fill the other with the name of each president
    for li in songs_list:
        num_list.append(li['Rank'])
        name_list.append(li['Song-Name'])
        # zip() is a built-in function that combines lists
        # creating a new list of tuples
    pairs_list = zip(num_list, name_list)
    # sort the list by the first item in each tuple, the number
    # pairs_list_sorted = sorted(pairs_list, key=lambda tup: int(tup[0]))
    return render_template('index.html', pairs=pairs_list, the_title="Songs Index")



@app.route('/songs/<num>')
def detail(num):
    for li in songs_list:
        if li['Rank'] == num:
            so_dict = li
            break
    return render_template('sochart.html', li=so_dict, the_title=so_dict['Song-Name'])
# your code here



# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
