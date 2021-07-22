from difflib import get_close_matches
import mysql.connector

# creating a dict out of the data.json file
# data = json.load(open("data.json"))

# connecting to the database
con = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

# creating a list of all words in the database
cursor = con.cursor()
query1 = cursor.execute("SELECT Expression from Dictionary")
keys = [b[0] for b in cursor.fetchall()]

# function that finds the def of word
def meaning(w):
    # cursor = con.cursor()
    query2 = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(w))
    results = cursor.fetchall()

    if results != []:
        return results
    elif results == [] and len(get_close_matches(w, keys)) > 0:
        maybe = get_close_matches(w, keys)[0]
        yn = input("Did you mean %s instead? (Y/N) " % maybe).lower()
        if yn == "y":
            query3 = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '{}'".format(maybe))
            new_results = cursor.fetchall()
            return new_results
        elif yn == "n":
            return "The word does not exist in the Dictionary!"
    else:
        return "The word does not exist in the Dictionary!"

#    w = w.lower()
#    if w in data:
#        return data[w]
#    elif w.title() in data:
#        return data[w.title()]
#    elif w.upper() in data:
#        return data[w.upper()]
#    elif len(get_close_matches(w, data.keys())) > 0:
#        maybe = get_close_matches(w, data.keys())[0]
#        yn = input("Did you mean %s instead? (Y/N) " % maybe).lower()
#        if yn == "y":
#            return data[maybe]
#        elif yn == "n":
#            return "The word does not exist in the Dictionary!"
#        else:
#            return "We didn't unserstand what you entered."
#    else:
#        return "The word does not exist in the Dictionary!"

# get user word and print its def
while True:
    user_input = input("Enter a word: ")
    output = meaning(user_input)
    
    if type(output) == list:
        for item in output:
            print(item)
    else:
        print(output)

    if(input("Do you want to continue? (Y/N) ").lower() == "n"):
        break
