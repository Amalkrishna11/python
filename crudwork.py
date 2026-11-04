
book = [
    {'id':"101", 'name':'Python Programming', 'author':'John Doe', 'category':'Programming', 'price':'500', 'number':'10'},
    {'id':"102", 'name':'Data Science', 'author':'Jane Smith', 'category':'Data', 'price':'600', 'number':'5'},
    {'id':"103", 'name':'Machine Learning', 'author':'Alice Johnson', 'category':'AI', 'price':'700', 'number':'8'},
    {'id':"104", 'name':'Deep Learning', 'author':'Bob Brown', 'category':'AI', 'price':'800', 'number':'3'},
    {'id':"105", 'name':'Web Development', 'author':'Charlie Davis', 'category':'Web', 'price':'400', 'number':'12'}
]

while True:
    choice = input("1.Add a book name\n2.Display Book name\n3.Update a Book name\n4.Remove a Book\n5.Search for a Book\n6.Exit\nEnter your choice:\t")

    match choice:

        case "1":
            id = input("Enter Book id:")
            name = input("Enter the Name:")
            author = input("Enter the Author:")
            category = input("Enter the Category:")
            price = input("Enter the Price:")
            number = input("Enter the Number of copies:")

            book.append({"id":id, "name":name, "author":author, "price":price, "category":category, "number":number})
            print("Book added successfully.")

        case "2":
            print(f"{'sl. No.':<20}{'id':<10}{'Name':<20}{'Author':<20}{'category':<20}{'Price':<10}{'Number of copies':<10}")

            for index, b in enumerate(book):
                print(f"{index+1:<20}{b['id']:<10}{b['name']:<20}{b['author']:<20}{b['category']:<20}{b['price']:<10}{b['number']:<10}")

            print(f"Total names:{len(book):>5}")

        case "3":
            print(f"{'sl. No.':<20}{'id':<10}{'Name':<20}{'Author':<20}{'category':<20}{'Price':<10}{'Number of copies':<10}")

            for index, b in enumerate(book):
                print(f"{index+1:<20}{b['id']:<10}{b['name']:<20}{b['author']:<20}{b['category']:<20}{b['price']:<10}{b['number']:<10}")

            edit_id = input("Enter the id of the name you want to edit:")

            for b in book:
                if b['id'] == edit_id:
                    b['name'] = input("Enter the new name:")
                    b['author'] = input("Enter the new author:")
                    b['category'] = input("Enter the new category:")
                    b['price'] = input("Enter the new price:")
                    b['number'] = input("Enter the new number of copies:")

                    print("Book details updated successfully.")
                    break
            else:
                print("Book not found.")

        case "4":
            print(f"{'sl. No.':<20}{'id':<10}{'Name':<20}{'Author':<20}{'category':<20}{'Price':<10}{'Number of copies':<10}")

            for index, b in enumerate(book):
                print(f"{index+1:<20}{b['id']:<10}{b['name']:<20}{b['author']:<20}{b['category']:<20}{b['price']:<10}{b['number']:<10}")

            delete_id = input("Enter the id of the name you want to delete:")

            for b in book:
                if b['id'] == delete_id:
                    book.remove(b)
                    print("Book removed successfully.")
                    break
            else:
                print("Book not found.")

        case "5":
            search_id = input("Enter the id of the name you want to search:")

            for index, b in enumerate(book):
                if b['id'] == search_id:
                    print(f"{'sl. No.':<20}{'id':<10}{'Name':<20}{'Author':<20}{'category':<20}{'Price':<10}{'Number of copies':<10}")
                    print(f"{index+1:<20}{b['id']:<10}{b['name']:<20}{b['author']:<20}{b['category']:<20}{b['price']:<10}{b['number']:<10}")
                    break
            else:
                print("Book not found.")

        case "6":
            print("Exiting the program.")
            break

        case _:
            print("Invalid choice.")
