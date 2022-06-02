from django.db import connection
 
def aboutissement():
    cursor = connection.cursor()
    return cursor