
from os import system
clear = lambda :system("cls")


from pickle import load
with open ("books.info","rb") as books_info:
    books = load(books_info)

#def add_to_excel
def add_book():
    clear()
    global books           #global list of all books
    book={}
    book["title"] = input("Enter title of the book: ")
    book["author"] = input("Enter author of the book :")
    book["pages"] = int(input ("Enter pages of the book: "))
    book["price"] =float(input ("Enter price of the book : "))
    book["isbn"] = input ("Enter ISBN of the book : ")
    books.append(book)




def list_books():
    clear()
    for book in books :
        print("-------------------------------------")
        print(f"Title : {book['title']}")
        print(f"Author : {book['author']}")
        print(f"Pages : {book['pages']}")
        print(f"Prices : {book['price']}")
        print(f"ISBN : {book['isbn']}")
        print("-------------------------------------")
    input("Press any key...")

        
#item_key = input("What is your search basis? : (title/author/pages/price/isbn)")
def find_book(): 
    clear()
    isbn = input("Enter ISBN to find your book :")
    for book in books:
        if book ["isbn"] == isbn :
            print("-------------------------------------")
            print(f"Title : {book['title']}")
            print(f"Author : {book['author']}")
            print(f"Pages : {book['pages']}")
            print(f"Prices : {book['price']}")
            print(f"ISBN : {book['isbn']}")
            print("-------------------------------------")
            input("Press any key...")
            break   #return True ham okeye
    else : 
        print("This book IS NOT in books database !")

#def myfind
    

def delete_book():
    clear()
    isbn = input("Enter ISBN to delete book :")
    for book in books :
        if book ["isbn"] == isbn :
            books.remove(book)
            input("Book has been deleted successfully")
            break
    else : 
        input("This book IS NOT in books database !")


def save_books():
    clear()
    from pickle import dump
    with open("books.info","wb") as books_info:
        dump(books,books_info)
        print("books has been saved succesfully")

