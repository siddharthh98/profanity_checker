
import urllib

def read_txt():
    quotes = open("/media/siddharth/Windows/Users/Siddharth/Desktop/movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_txt(contents_of_file)
    
def check_txt(text_file):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_file)
    response = connection.read()
    #print (response)
    connection.close()
    if "true" in response:
        print("Profanity Alert!!")
    elif "false" in response:
        print("This document has no curse words!")
    else:
        print("Please insert some text first")
read_txt()
