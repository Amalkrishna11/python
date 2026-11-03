book = [{'id':"101" ,'name':'Python Programming' , 'author':'John Doe','category': 'Programming','price':'500','number':'10' },{'id':"102" ,'name':'Data Science' , 'author':'Jane Smith','category': 'Data','price':'600','number':'5' },
        {'id':"103" ,'name':'Machine Learning' , 'author':'Alice Johnson','category': 'AI','price':'700','number':'8' },
        {'id':"104" ,'name':'Deep Learning' , 'author':'Bob Brown','category': 'AI','price':'800','number':'3' },
        {'id':"105" ,'name':'Web Development' , 'author':'Charlie Davis','category': 'Web','price':'400','number':'12' }]



while True:
    choice = input("1.Add a book name\n2.Display Book name\n3.Update a Book name\n4.Remove a Book\n5.Search for a Book\n6.Exit\nEnter your choice:\t")
    match choice:
        case "1":   
            id = input("Enter Book id:")
            name = input ("Enter the Name:")
            author = input("Enter the Author: ")
            category = input("Enter the Category:")
            price = input("Enter the Price:")
            number = input("Enter the Number of copies:")
            book.append({"id":id,"name":name,"author":author,"price":price,"category":category,"number":number})
        case "2":
            print(f"{'sl. No.':<20}{'id':<4}{'Name':<20}{'Author':<20}{'1category':<20}{'Price':<10}{'Number of copies':<10}")
            for index,book in enumerate(book):
                print(f"{index+1:<20}{book['id']:<4}{book['name']:<20}{book['author']:<20}{book['category']:<20}{book['price']:<10}{book['number']:<10}")
            print(f"Total names:{len(book):>5}")
        case "3":
            print(f"{'sl. No.':<20}{'id':<4}{'Name':<20}{'Author':<20}{'1category':<20      }{'Price':<10}{'Number of copies':<10}")
            for index,book in enumerate(book):
                print(f"{index+1:<20}{book['id']:<4}{book['name']:<20}{book['author']:<20}{book['category']:<20}{book['price']:<10}{book['number']:<10}")
            edit_id = (input("Enter the id of the name you want to edit:"))
            for book in book:
                if book['id'] == edit_id:
                    book['name'] = input("Enter the name:")
                    book['author'] = input("enter the author:")
                    book['category'] = input("Enter the category:")
                    book['price'] = input("Enter the price:")
                    book['number'] = input("Enter the number of copies:")
        case "4":
            print(f"{'sl. No.':<20}{'id':<4}{'Name':<20}{'Author':<20}{'1category':<20}{'Price':<10}{'Number of copies':<10}")
            for index,book in enumerate(book):
                print(f"{index+1:<20}{book['id']:<4}{book['name']:<20}{book['author']:<20}{book['category']:<20}{book['price']:<10}{book['number']:<10}")   
            delete_id = input("enter the id of the book you want to remove:")
            for book in book:
                if book['id']== delete_id:
                    book.remove(book)
                    print("Book removed successfully.")
        case "5":
            search_id = input("Enter the id of the book you want to search for:")
            found = False
            for book in book:
                if book['id'] == search_id:
                    print(f"Book found:{book}")
                    found = True
                    break
            if not found:
                print("Book not found.")
        case "6":
            print("Exiting..")
            break
        case _: 
            print("Invalid Entry")      
