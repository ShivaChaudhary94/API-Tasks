# Fetch Users from Public API (Beginner Task)

This Python script fetches a list of users from a public API and displays their details in a clean format.

---

## 🧠 Task Description
The script performs the following:
1. Fetches data using a GET request from the API endpoint:  
   `https://jsonplaceholder.typicode.com/users`
2. Displays for each user:
   - Name  
   - Username  
   - Email  
   - City (from address.city)
3. Prints users whose city starts with 'S' (Bonus feature).
4. Handles possible errors (like failed requests).

---

## 🛠️ Requirements
Make sure you have Python installed (Python 3+).

You’ll also need the **requests** library.  
Install it using:

```bash
pip install requests
