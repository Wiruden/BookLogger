const divC = document.getElementById("CompletedBooks");
const divR = document.getElementById("ReadingBooks");
const divP = document.getElementById("PlannedBooks");
const logButton = document.getElementById("logBook");
const bookInput = document.getElementById("bookIn");

// Function to fetch data from Python
async function loadBooks() {
    divC.innerHTML = "";
    divR.innerHTML = "";
    divP.innerHTML = "";

    try {
        const response = await fetch("http://127.0.0.1:5000/get_books");
        const data = await response.json();

        // PASS THE STATUS STRING HERE!
        data.completed.forEach(line => createBookElement(line, divC, "completed"));
        data.reading.forEach(line => createBookElement(line, divR, "reading"));
        data.planned.forEach(line => createBookElement(line, divP, "planned"));

    } catch (error) {
        console.error("Error:", error);
        alert("Error")
    }
}

function createBookElement(textLine, container, currentStatus) {
    // 1. Parse Title
    let titlePart = textLine.split(",")[0]; 
    let bookTitle = titlePart.replace("Title: ", "").trim();

    // 2. Card Wrapper
    let card = document.createElement("div");
    card.classList.add("book-card");

    // 3. Info
    let infoDiv = document.createElement("div");
    infoDiv.classList.add("book-info");
    
    let textP = document.createElement("p");
    textP.textContent = textLine;
    textP.classList.add("book-title");
    infoDiv.appendChild(textP);

    // 4. Dropdown
    let dropdownDiv = document.createElement("div");
    dropdownDiv.classList.add("dropdown");

    let editBtn = document.createElement("button");
    editBtn.classList.add("editButton");
    editBtn.onclick = function(event) {
        closeAllDropdowns();
        document.getElementById("dropdown-" + bookTitle.replace(/\s+/g, '')).classList.toggle("show");
        event.stopPropagation();
    };

    let menuDiv = document.createElement("div");
    // Remove spaces from ID to prevent errors
    menuDiv.id = "dropdown-" + bookTitle.replace(/\s+/g, ''); 
    menuDiv.classList.add("dropdown-content");

    // --- FIX IS HERE: Passing currentStatus correctly ---
    
    if (currentStatus !== "reading") {
        let btn = document.createElement("button");
        btn.textContent = "Move to Reading";
        btn.classList.add("btn-move");
        // We pass currentStatus explicitly here
        btn.onclick = () => moveBook(bookTitle, currentStatus, "reading");
        menuDiv.appendChild(btn);
    }

    if (currentStatus !== "completed") {
        let btn = document.createElement("button");
        btn.textContent = "Move to Completed";
        btn.classList.add("btn-move");
        btn.onclick = () => moveBook(bookTitle, currentStatus, "completed");
        menuDiv.appendChild(btn);
    }

    if (currentStatus !== "planned") {
        let btn = document.createElement("button");
        btn.textContent = "Move to Planned";
        btn.classList.add("btn-move");
        btn.onclick = () => moveBook(bookTitle, currentStatus, "planned");
        menuDiv.appendChild(btn);
    }

    let btnDel = document.createElement("button");
    btnDel.textContent = "Delete";
    btnDel.classList.add("btn-delete");
    btnDel.onclick = () => deleteBook(bookTitle);
    menuDiv.appendChild(btnDel);

    dropdownDiv.appendChild(editBtn);
    dropdownDiv.appendChild(menuDiv);
    card.appendChild(infoDiv);
    card.appendChild(dropdownDiv);
    container.appendChild(card);
}

async function deleteBook(title) {
    if(!confirm(`Delete "${title}"?`)) return;

    await fetch("http://127.0.0.1:5000/delete_book", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title: title })
    });
    loadBooks(); // Refresh UI
}

async function moveBook(title, oldStatus, newStatus) {
    await fetch("http://127.0.0.1:5000/move_book", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
            title: title,
            old_status: oldStatus,
            new_status: newStatus
        })
    });
    loadBooks(); // Refresh UI
}

// Close dropdowns if user clicks anywhere else
window.onclick = function(event) {
    if (!event.target.matches('.editButton')) {
        closeAllDropdowns();
    }
}

function closeAllDropdowns() {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
            openDropdown.classList.remove('show');
        }
    }
}

// Function to send data to Python
logButton.addEventListener("click", async function() {
    const title = bookInput.value;
    if (!title) return alert("Please enter a name");

    // Send data to Python
    await fetch("http://127.0.0.1:5000/log_book", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ 
            title: title, 
            status: "planned" // Defaulting to planned for now
        })
    });

    bookInput.value = ""; // Clear input
    loadBooks(); // Refresh list
});

// Load books when page opens
loadBooks();