Books_all = []  # List to store book details

# Function to load books from file
def load_books():
    try:
        with open("books.txt", "r") as file:
            for line in file:
                data = line.strip().split(" | ")
                if len(data) == 5:
                    Books_all.append({
                        "Name": data[0],
                        "Author": data[1],
                        "Publication": data[2],
                        "Genre": data[3],
                        "Read": data[4]
                    })
    except FileNotFoundError:
        pass  # If file doesn't exist, no books are loaded

# Function to save books to file
def save_books():
    with open("books.txt", "w") as file:
        for book in Books_all:
            file.write(f"{book['Name']} | {book['Author']} | {book['Publication']} | {book['Genre']} | {book['Read']}\n")

# Load books from file at the start
load_books()

while True:
    # Display menu options
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")
    
    user_inp = int(input("Enter your Choice: "))  # Get user choice
    
    if user_inp == 1:
        # Add a book
        book_Name = input("Enter the book title: ")
        book_author = input("Enter the author: ")
        book_publication = input("Enter the publication year: ")
        book_genre = input("Enter the genre: ")
        book_read = input("Have you read this book? (yes/no): ").strip().lower()
        
        books_data = {
            "Name": book_Name,
            "Author": book_author,
            "Publication": book_publication,
            "Genre": book_genre,
            "Read": "Read" if book_read == "yes" else "Unread"
        }
        
        Books_all.append(books_data)  # Add book to list
        save_books()  # Save updated list to file
        print("✅ Book added successfully!")
    
    elif user_inp == 2:
        # Remove a book
        find_book = input("Enter the title of the book to remove: ").strip()
        book_found = None

        for book in Books_all:
            if book["Name"].lower() == find_book.lower():
                book_found = book
                break

        if book_found:
            Books_all.remove(book_found)
            save_books()  # Save updated list to file
            print("✅ Book removed successfully!")
        else:
            print("❌ Book Not Found!")
    
    elif user_inp == 3:
        # Search for a book
        search_choice = input("Search by (1) Title or (2) Author: ").strip()
        
        if search_choice == "1":
            title = input("Enter the title: ").strip()
            found_books = [book for book in Books_all if book["Name"].lower() == title.lower()]
        elif search_choice == "2":
            author_name = input("Enter the Author Name: ").strip()
            found_books = [book for book in Books_all if book["Author"].lower() == author_name.lower()]
        else:
            print("❌ Invalid choice! Please enter 1 or 2.")
            continue

        # Display search results
        if found_books:
            for index, book in enumerate(found_books, start=1):
                print(f"{index}. {book['Name']} by {book['Author']} ({book['Publication']}) - {book['Genre']} - {book['Read']}")
        else:
            print("❌ No matching books found!")
    
    elif user_inp == 4:
        # Display all books
        if not Books_all:
            print("\n📚 Library is empty! No books to display.")
        else:
            print("\n📖 List of Books in the Library:")
            for index, book in enumerate(Books_all, start=1):
                print(f"{index}. {book['Name']} by {book['Author']} ({book['Publication']}) - {book['Genre']} - {book['Read']}")
    
    elif user_inp == 5:
        # Display statistics
        total_books = len(Books_all)
        if total_books == 0:
            print("\n📊 No books in the library yet!")
        else:
            read_books = sum(1 for book in Books_all if book["Read"] == "Read")
            percentage_read = (read_books / total_books) * 100
            print(f"\n📊 Total Books: {total_books}")
            print(f"📖 Percentage of Books Read: {percentage_read:.2f}%")
    
    elif user_inp == 6:
        # Exit program
        print("\n👋 Exiting the Library Manager. Goodbye!")
        break
    else:
        print("❌ Invalid choice! Please enter a number between 1-6.")
