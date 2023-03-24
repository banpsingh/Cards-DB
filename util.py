from app import mysql

def get_recent_decks(n):
  """
  Returns the 'n' most recent rows added to the 'decks' sql table

  Each row is a tuple and the entire result is wrapped in a large tuple.
  """
  cursor = mysql.connection.cursor()
  cursor.execute('''SELECT * FROM decks 
                    ORDER BY date_added DESC LIMIT %s''', (n,))
  rows=cursor.fetchall()
  cursor.close()
  return rows


def get_random_deck():
  """
  Returns one random row from the 'decks' sql table
  """
  cursor = mysql.connection.cursor()
  cursor.execute('''SELECT * FROM decks
                    ORDER BY RAND()
                    LIMIT 1''')
  rows=cursor.fetchall()
  cursor.close()
  return rows


def get_num_decks():
  """
  Returns the total number of entries in the 'decks' sql table
  """
  cursor = mysql.connection.cursor()
  cursor.execute('''SELECT COUNT(id) FROM decks''')
  total=cursor.fetchall()
  cursor.close()
  return total

def get_num_distinct_designers():
  """
  Returns the number of distinct desingers in the 'decks' sql table
  """
  cursor = mysql.connection.cursor()
  cursor.execute('''SELECT COUNT( DISTINCT(designer)) FROM decks''')
  total=cursor.fetchall()
  cursor.close()
  print("total",total)
  return total


def get_month_decks():
  """
  Returns the number of entries added to the 'decks' sql table this month
  """
  cursor = mysql.connection.cursor()
  cursor.execute('''SELECT COUNT(*) FROM decks 
                    WHERE month(date_added)=month(now())''')
  total=cursor.fetchall()
  cursor.close()
  return total


def get_all_decks():
  """
  Returns all the rows of the 'decks' sql table.

  The returned result is a tuple containing tuples (rows).
  """
  cursor = mysql.connection.cursor()
  cursor.execute('''SELECT * FROM decks ''')
  rows=cursor.fetchall()
  cursor.close()
  return rows


def upload_deck(request, image_name):
  """
  Adds a new row into the 'decks' sql table with values from 'request' and 
  'image_name'.

  Parameter request: An object containing user input form data such as 
                     'manufacturer', 'deck_name', 'designer', and 'year_released'.
  
  Parameter image_name: A string containing the name of the image file uploaded.
  """
  image_path = 'images/' + image_name
  manufacturer = request.form['manufacturer'] \
                 if request.form['manufacturer_list'] == "other" \
                 else request.form['manufacturer_list']
  cursor = mysql.connection.cursor()
  cursor.execute(''' INSERT INTO decks(deck_name, designer, manufacturer, 
                     year_made, deck_image_path) 
                     VALUES(%s,%s,%s,%s,%s)''',
                 (request.form['deck_name'],request.form['designer'],
                  manufacturer,request.form['year_released'],
                  image_path))
  mysql.connection.commit()
  cursor.close()


def delete_deck_by_id(deck_id):
  """
  Deletes the row from the 'decks' table with the 'id' field equal to the
  'deck_id' passed to this function.
  
  Parameter deck_id: The id of the row to delete from 'decks'.
  Precondition: deck_id is an int that exists in 'decks'.
  """
  cursor = mysql.connection.cursor()
  cursor.execute('''DELETE FROM decks WHERE id=%s''',(deck_id,))
  mysql.connection.commit()
  cursor.close()


def get_filename_by_id(deck_id):
  """
  Returns the path to the image file of the deck specified by 'deck_id' from the 
  'decks' sql table.
  
  Example:
      If the image is called 'picture.jpeg', this function will return
      'images/picture.jpeg'
    
  Parameter deck_id: The id of the row of interest.
  Precondition: deck_id is an int that exists in 'decks'.
  """
  cursor = mysql.connection.cursor()
  cursor.execute('''SELECT deck_image_path FROM decks WHERE id=%s ''',(deck_id,))
  name=cursor.fetchall()
  cursor.close()
  return name


def get_one_deck_by_id(deck_id):
  """
  Returns the row of the deck specified by 'deck_id' from the 'decks' sql table.
    
  Parameter deck_id: The id of the row of interest.
  Precondition: deck_id is an int that exists in 'decks'.
  """
  cursor = mysql.connection.cursor()
  cursor.execute('''SELECT * FROM decks WHERE id=%s ''',(deck_id,))
  rows=cursor.fetchall()
  cursor.close()
  return rows


def update_deck_same_image(request, deck_id):
  """
  Updates the row in 'decks' specified by 'deck_id' with data from 'request'.
  This function DOES NOT change the image file in 'decks'.

  Parameter request: An object containing user input form data such as 
                     'manufacturer', 'deck_name', 'designer', and 'year_released'.
  
  Parameter deck_id: The id of the row of interest.
  """
  manufacturer = request.form['manufacturer'] \
                 if request.form['manufacturer_list'] == "other" \
                 else request.form['manufacturer_list']
  cursor = mysql.connection.cursor()
  cursor.execute('''UPDATE decks 
                    SET deck_name = %s, designer = %s, manufacturer = %s, 
                    year_made = %s
                    WHERE id = %s''',
                  (request.form['deck_name'],request.form['designer'],
                  manufacturer,request.form['year_released'], deck_id))
  mysql.connection.commit()
  cursor.close()


def update_deck_new_image(request, deck_id, image_name):
  """
  Updates the row in 'decks' specified by 'deck_id' with data from 'request'.
  This function DOES change the image file in 'decks' with the new image 
  specified by 'filename'

  Parameter request: An object containing user input form data such as 
                     'manufacturer', 'deck_name', 'designer', and 'year_released'.
  
  Parameter deck_id: The id of the row of interest.

  Parameter image_name: A string containing the name of the image file uploaded.
  """
  image_path = 'images/' + image_name
  manufacturer = request.form['manufacturer'] \
                 if request.form['manufacturer_list'] == "other" \
                 else request.form['manufacturer_list']
  cursor = mysql.connection.cursor()
  cursor.execute('''UPDATE decks 
                    SET deck_name = %s, designer = %s, manufacturer = %s, 
                    year_made = %s, deck_image_path = %s
                    WHERE id = %s''',
                  (request.form['deck_name'],request.form['designer'],
                  manufacturer,request.form['year_released'], image_path, deck_id))
  mysql.connection.commit()
  cursor.close()