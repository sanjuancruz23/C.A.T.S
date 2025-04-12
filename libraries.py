import requests

def book_search(bookName):

    #Splits up the title and rejoins them with '+' for the API
    query = bookName.split()
    lookup = "+".join(query)



if __name__ == '__main__':
    book_search("Your Mom house")