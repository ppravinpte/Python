import difflib # nn
from difflib import get_close_matches

import mysql.connector
con = mysql.connector.connect(
    user= "ardit700_student",
    password =  "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

cursor = con.cursor()

key = input("enter word for meaning:")
keylower = key.lower()
keyupper = key.upper()
keytitle = key.title()
query = cursor.execute("select * from Dictionary where expression in ('%s','%s','%s') " % (keylower,keyupper,keytitle))
outputs = cursor.fetchall()
if outputs:
    for output in outputs:
        print (output[1])   # Dictionary has Expression and Definition columns. need only 2nd so kept [1]
else:
    #query = cursor.execute("SELECT Expression FROM Dictionary WHERE Expression LIKE '{}%' AND length(Expression)<{}".format(key[:-1],len(key)+1))
    query = cursor.execute("SELECT Expression FROM Dictionary")
    new_result=[records[0] for records in cursor.fetchall()]

    if len(get_close_matches(key, new_result)) > 0:
        revised_val = get_close_matches(key, new_result)

        choice = input("do you want to type:{}. if yes then type Y/N:".format(revised_val[0]))
        if choice.lower() == 'y':
            query1 = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '{}'".format(revised_val[0]))
            #<other format> query1 = cursor.execute("SELECT Definition FROM Dictionary WHERE Expression = '%s'" % revised_val[0]) 
            output_new = cursor.fetchall()
            if output_new:
                for outputn in output_new:
                    print (outputn[0])
            else:
                print ('error in fetching value')
        elif choice.lower() == 'n': 
            print ("no matching record found. Please try entering other word next time")
        else:
            print ("Valid values are Y/N so request is not processed" )
    else:
        print ('No record found.')