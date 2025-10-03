books=["harry potter by jk rowling","the alchemist by paulo coelho","the great gatsby by f scott fitzgerald"]
while True:
    print("1. Add new book")
    print("2. Remove book")
    print("3. Search book by title")
    print("4. Display all books")
    print("5. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        updated_books = books.append(input("Enter book title and author:").lower())
        print(f" The book has added to the list of {books} successfully.")
    elif choice==2:
        book_to_remove = books.remove(input("Enter book title and author to remove:").lower())
        print(f"The book has removed from the list of {books} successfully.")
    elif choice==3:
        search_title = input("Enter book title to search:").lower()
        found = False
        for book in books:
            if search_title in book:
                print(f"Book found: {book}")
                found = True
                break
        if not found:
            print("Book not found.")
    elif choice==4:
        display_books = books
        print(f"List of books:{display_books}")
    elif choice==5:
        print("Exit the digital library! Thank you!")
        break
    else:
        print("Invalid choice. Please try again.")
        