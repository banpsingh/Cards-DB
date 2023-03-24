import os
import util
import config
from flask import Flask, flash, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = './static/images'


app = Flask(__name__)
app.secret_key = config.secret_key

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = config.mysql_pw
app.config['MYSQL_DB'] = config.db_name
 
mysql = MySQL(app)


@app.route("/")
def base():
  """
  Fetch all of the information from the homepage and pass it to the template. 
  """
  recent_decks = util.get_recent_decks(3)
  random_deck = util.get_random_deck()
  total_num_decks = util.get_num_decks()
  total_month_decks = util.get_month_decks()
  num_diff_designer = util.get_num_distinct_designers()
  context = {'recent_decks':recent_decks, 
             'random_deck':random_deck, 
             'total_num_decks':total_num_decks,
             'num_diff_designer':num_diff_designer,
             'total_month_decks':total_month_decks}
  return render_template('base.html', context=context)


@app.route("/upload/", methods=['GET', 'POST'])
def upload_deck():
  """
  GET request: Renders the upload template
  
  POST request: Uploads the deck information to the 'decks' sql table and saves
                the image file to 'static/images'.
  """
  if request.method == 'GET':
    return render_template('upload.html')
  elif request.method == 'POST':
    if 'deck_image' not in request.files:
      flash('No file part')
      return redirect(request.url)
    file = request.files['deck_image']
      # If the user does not select a file, the browser submits an
      # empty file without a filename.
    if file.filename == '':
      flash('No selected file')
      return redirect(request.url)
    if file:
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      util.upload_deck(request, filename)
      flash('Deck Upload Successful!')
      return redirect(request.url)


@app.route("/collection/", methods=['GET', 'POST'])
def collection_display():
  """
  Fetches and displays all the decks in 'decks'
  """
  rows = util.get_all_decks()
  return render_template('collection.html', rows=rows)


@app.route("/collection/delete/<int:deck_id>")
def delete_deck(deck_id):
  """
  Deletes the deck specified by 'deck_id', deletes the image file from 
  'static/images', and redirects the user to the collection route.
  """
  filename = util.get_filename_by_id(deck_id)[0][0]
  util.delete_deck_by_id(deck_id)
  os.remove(os.path.join('./static/', filename))
  return redirect(url_for('collection_display'))
 

@app.route("/collection/update/<int:deck_id>", methods=['GET', 'POST'])
def update_deck(deck_id):
  """
  GET request: Renders the update form specified by 'deck_id'
  
  POST request: Updates the 'decks' table with form data and updates 
  'static/images' if a new image was uploaded.
  """
  if request.method == 'GET':
    deck_info = util.get_one_deck_by_id(deck_id)
    return render_template('update_deck.html', deck_info=deck_info)
  else:
    file = request.files['deck_image']
    if file.filename == '':
      util.update_deck_same_image(request, deck_id)
    else:
      # remove old image
      image_path = util.get_filename_by_id(deck_id)[0][0]
      os.remove(os.path.join('./static/', image_path))
      # insert new image 
      if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      util.update_deck_new_image(request, deck_id, filename)
    return redirect(url_for('collection_display'))
 
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4999, debug=True)



