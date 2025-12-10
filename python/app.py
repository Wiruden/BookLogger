import os
import datetime
from flask import Flask, jsonify, request
from flask_cors import CORS
import webbrowser
from threading import Timer

app = Flask(__name__)
CORS(app)  # Allows the website to talk to this script

dir_name = "Book Logs"

# --- HELPER FUNCTIONS ---

def ensure_files_exist():
    """Creates the folder and text files if they don't exist"""
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    
    files = ["Completed_Books_Log.txt", "Reading_Books_Log.txt", "Planned_Books_Log.txt"]
    for f in files:
        file_path = os.path.join(dir_name, f)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as file:
                # Write the filename as the header
                file.write(f"{f}\n")

def get_filename(status):
    if not status: return "Planned_Books_Log.txt" # Default if None
    status = status.lower() 
    if status == "completed": return "Completed_Books_Log.txt"
    if status == "reading": return "Reading_Books_Log.txt"
    if status == "planned": return "Planned_Books_Log.txt"
    return "Planned_Books_Log.txt"

def read_file_lines(filename):
    """Reads a file and returns the lines (skipping the header)"""
    file_path = os.path.join(dir_name, filename)
    lines_content = []
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # Skip the first line (header) using slice [1:]
            for row in lines[1:]:
                clean_row = row.strip()
                if clean_row:
                    lines_content.append(clean_row)
    return lines_content

# --- FLASK ROUTES (The Bridge to your Website) ---

@app.route('/get_books', methods=['GET'])
def get_books():
    """Sends all 3 lists to the website"""
    ensure_files_exist()
    data = {
        "completed": read_file_lines("Completed_Books_Log.txt"),
        "reading": read_file_lines("Reading_Books_Log.txt"),
        "planned": read_file_lines("Planned_Books_Log.txt")
    }
    return jsonify(data)

@app.route('/log_book', methods=['POST'])
def log_book_route():
    """Logs a new book"""
    data = request.json
    title = data.get('title')
    status = data.get('status', 'planned')
    
    filename = get_filename(status)
    path = os.path.join(dir_name, filename)
    date = datetime.datetime.now().strftime("%x")
    
    # We add a comma after the title to make reading/deleting easier later
    with open(path, 'a') as f:
        f.write(f"Title: {title}, Added: {date}\n")
    
    print(f"Logged {title} to {filename}")
    return jsonify({"message": "Success"})

@app.route('/delete_book', methods=['POST'])
def delete_book_route():
    """Deletes a book from ALL lists"""
    data = request.json
    title = data.get('title')
    
    files = ["Completed_Books_Log.txt", "Reading_Books_Log.txt", "Planned_Books_Log.txt"]
    
    for fname in files:
        path = os.path.join(dir_name, fname)
        if not os.path.exists(path): continue
        
        # Read all lines
        with open(path, 'r') as f:
            lines = f.readlines()
            
        # Write back only lines that DON'T match the title
        new_lines = []
        for line in lines:
            # We check for "Title: {title}," with a comma to be exact
            if f"Title: {title}," not in line:
                new_lines.append(line)
                
        with open(path, 'w') as f:
            f.writelines(new_lines)

    return jsonify({"message": "Deleted"})

@app.route('/move_book', methods=['POST'])
def move_book_route():
    """Moves a book from one list to another"""
    data = request.json
    title = data.get('title')
    old_status = data.get('old_status')
    new_status = data.get('new_status')

    # 1. Delete from OLD file
    old_file = get_filename(old_status)
    old_path = os.path.join(dir_name, old_file)
    
    if os.path.exists(old_path):
        with open(old_path, 'r') as f:
            lines = f.readlines()
        
        new_lines = []
        for line in lines:
            if f"Title: {title}," not in line:
                new_lines.append(line)
        
        with open(old_path, 'w') as f:
            f.writelines(new_lines)

    # 2. Add to NEW file
    new_file = get_filename(new_status)
    new_path = os.path.join(dir_name, new_file)
    date = datetime.datetime.now().strftime("%x")
    
    with open(new_path, 'a') as f:
        f.write(f"Title: {title}, Added: {date}\n")

    print(f"Moved {title} from {old_status} to {new_status}")
    return jsonify({"message": "Moved successfully"})

def open_browser():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    html_path = os.path.join(script_dir, '..', 'website', 'index.html')
    
    html_path = os.path.abspath(html_path)
    
    print(f"Opening website at: {html_path}")
    
    webbrowser.open_new(html_path)

# --- START THE SERVER ---
if __name__ == '__main__':
    ensure_files_exist()
    print("Server is running on port 5000...")
    
    if not os.environ.get("WERKZEUG_RUN_MAIN"):
        Timer(1, open_browser).start()
    
    app.run(debug=True, port=5000)