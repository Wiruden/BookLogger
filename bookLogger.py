import os
import re

dir_name = "Book Logs"

#creates the folder
def create_log_directory(dir_name):
    if(not os.path.exists(dir_name)):
        os.mkdir(dir_name)
    
#creates txt log file for completed books
def create_completed_log_file(dir_name):
    file_name = "Completed_Books_Log.txt"
    file_path = os.path.join(dir_name, file_name)
    
    if(not os.path.exists(file_path)):
        with open(file_path, 'w') as file:
            file.write("Completed Books Log\n")
        print("Completed books Log file created.")
    ##else:
    ##    print("Completed books Log file already exists.")

#creates txt log file for currently reading books
def create_reading_log_file(dir_name):
    file_name = "Reading_Books_Log.txt"
    file_path = os.path.join(dir_name, file_name)
    
    if(not os.path.exists(file_path)):
        with open(file_path, 'w') as file:
            file.write("Reading Books Log\n")
        print("Reading books Log file created.")
    ##else:
    ##    print("Reading books Log file already exists.")
    
#creates txt log file for planned to read books    
def create_planned_log_file(dir_name):
    file_name = "Planned_Books_Log.txt"
    file_path = os.path.join(dir_name, file_name)
    
    if(not os.path.exists(file_path)):
        with open(file_path, 'w') as file:
            file.write("Planned Books Log\n")
        print("Planned books Log file created.")
    ##else:
    ##    print("Planned books Log file already exists.")

#creates the directory and log files
create_log_directory(dir_name)
create_completed_log_file(dir_name)
create_reading_log_file(dir_name)
create_planned_log_file(dir_name)
        
def get_filename(status):
    if(status.lower() == "completed"):
        file_name = "Completed_Books_Log.txt"
    elif(status.lower() == "reading"):
        file_name = "Reading_Books_Log.txt"
    elif(status.lower() == "planned"):
        file_name = "Planned_Books_Log.txt"
    return file_name
    
#logs books
def log_book(book_title, pages_read, status, file_name):
    if(status == "reading"):
        print(f"Logging Book: {book_title}, Pages read: {pages_read}, Status: {status}, to {file_name}")
    else:
        print(f"Logging Book: {book_title}, Status: {status}, to {file_name}")
    
    file_path = os.path.join(dir_name, file_name)
    
    with open(file_path, 'a') as file:
        if(pages_read > 0):
            file.write(f"Title: {book_title}, Pages Read: {pages_read}\n")
        else:
            file.write(f"Title: {book_title}\n")
    

def delete_helper(file_path, book_title):
    with open(file_path, 'r') as file:
        found = False
        lines = file.readlines()
        lines_to_keep = []
        for row in lines:
            if(row.strip().startswith(f"Title: {book_title}")):
                found = True
            else:
                lines_to_keep.append(row)
                
        if(found):
            with open(file_path, 'w') as file:
                print(f"Deleting '{book_title}'")
                file.writelines(lines_to_keep)
        else:
            print(f"Could not find {book_title}")



#Deletes books
def delete_book(book_title):
    completed_file = "Completed_Books_Log.txt"
    reading_file = "Reading_Books_Log.txt"
    plan_file = "Planned_Books_Log.txt"
    
    #COMPLETED
    delete_helper(os.path.join(dir_name, completed_file), book_title)
    #READING
    delete_helper(os.path.join(dir_name, reading_file), book_title)
    #PLANNED
    delete_helper(os.path.join(dir_name, plan_file), book_title)
    
    
    
    
    '''with open(completed_path, 'r') as file:
        found = False
        lines = file.readlines()
        lines_to_keep = []
        for row in lines:
            if(row.strip().startswith(f"Title: {book_title}")):
                found = True
            else:
                lines_to_keep.append(row)
                
        if(found):
            with open(completed_path, 'w') as file:
                print(f"Deleting '{book_title}'")
                file.writelines(lines_to_keep)
        else:
            print(f"The title '{book_title}' is not in the completed books file.")
    
    #READING
    with open(reading_path, 'r') as file:
        found = False
        lines = file.readlines()
        lines_to_keep = []
        for row in lines:
            if(row.strip().startswith(f"Title: {book_title}")):
                found = True
            else:
                lines_to_keep.append(row)
                
        if(found):
            with open(reading_path, 'w') as file:
                print(f"Deleting '{book_title}'")
                file.writelines(lines_to_keep)
        else:
            print(f"The title '{book_title}' is not in the reading books file.")

    #PLANNED
    with open(plan_path, 'r') as file:
        found = False
        lines = file.readlines()
        lines_to_keep = []
        for row in lines:
            if(row.strip().startswith(f"Title: {book_title}")):
                found = True
            else:
                lines_to_keep.append(row)
                
        if(found):
            with open(plan_path, 'w') as file:
                print(f"Deleting '{book_title}'")
                file.writelines(lines_to_keep)
        else:
            print(f"The title '{book_title}' is not in the planned books file.")'''

#Changes the page number
def edit_pages(book_title, pages_read):
    file_name = "Reading_Books_log.txt"
    file_path = os.path.join(dir_name,file_name)
    lines_to_keep = []
    found = False
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        for row in lines:
            if(row.strip().startswith(f"Title: {book_title}")):
                book_line = row.strip()
                found = True
            else:
                lines_to_keep.append(row)
            
        
                
    
    if(found):
        updated_line = re.sub(r', Pages Read: \d+', f', Pages Read: {pages_read}', book_line)
        
        lines_to_keep.append(updated_line + '\n')
        with open(file_path, 'w') as file:
            file.writelines(lines_to_keep)
    else:
        print(f"Could not find: {book_title}")
        
#Shows the whole list
def show_list(file_name):  
    file_path = os.path.join (dir_name, file_name)
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        index = 0
        for row in lines:
            if(index >= 1):
                print(f"{index} {row}")
            index += 1
        

while True:
    choice = input("1. Log a book 2. Delete a book 3. Edit pages 4. View a file(Press 'X' to exit) ")
    
    if(choice == "1"):
        pages_read = ""

        book_title = input("Book Title: ")
        while True:
            status = input("Status (Completed, Reading, Planned): ")
            if(status.lower() == "completed" or status.lower() == "reading" or status.lower() == "planned"):
                break
            else:
                print("Invalid status. Please enter Completed, Reading, or Planned.")
            
        if(status.lower() == "reading"):
            pages_read = input("Pages Read: ")
            
        log_book(book_title, pages_read, status, get_filename(status))
    
    elif(choice == "2"):
        book_title = input("Title of the book you want to delete: ")
        delete_book(book_title)
        
    elif(choice == "3"):
        book_title = input("Title of the book you want to edit: ")
        pages_read = input("Number of pages you read: ")
        edit_pages(book_title, pages_read)
    
    elif(choice.lower() == "x"):
        break
    
    elif(choice == "4"):
        while True:
            status = input("Which file do you want to look at (Completed, Reading, Planned)")
            if(status.lower() == "completed" or status.lower() == "reading" or status.lower() == "planned"):
                break
            else:
                print("Invalid status. Please enter Completed, Reading, or Planned.")
        show_list(get_filename(status))