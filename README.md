# Modern Garments - Inventory & Billing Management System

An Inventory, Billing, and Ledger Tracking software built for garment businesses using **Python (Tkinter)** and **MySQL**. Developed by **Uzair Ahamed. M** under the guidance of **Shankar. [cite_start]D**[cite: 32, 34, 35].

---

## 📸 Project Interface & Features Breakdown

To see how the application works, here are the screenshots of the main interfaces alongside their associated layout assets:

### 1. User Authentication System
* **File Asset:** `user.png`, `pass.png`, `mail.png`, `phone.png`, `eye1.png`, `eye2.png`
* **What it does:** This is the secure gateway for the system. Users can register a new profile or log in. It features dynamic text fields that clear upon clicking and password visibility toggles (`show="*"`) using the eye icons to ensure security.

### 2. Async Loading Splash Screen
* **File Asset:** `lpage.png`
* **What it does:** When a user successfully logs in, a smooth loading bar appears. It uses Python multi-threading (`threading.Thread`) to keep the interface responsive while securely communicating with the MySQL database backend in the background.

### 3. Main Dashboard Terminal
* **File Asset:** `hpage.png`, `hme.png`, `prfl.png`
* **What it does:** The central control hub of the application. It dynamically pulls the active logged-in username to personalize the screen, shows the current real-time system date, and gives quick button links to all different business modules.

### 4. Live Stock Inventory Manager
* **File Asset:** `stk.png`
* **What it does:** Allows the business to Add, View, Update, or Delete products from the database instantly. Every time an item is modified, deleted, or added, it logs the operational status into an automated background audit list to track changes.

### 5. Stock Inventory Spreadsheet View
* **File Asset:** `optn.png`
* **What it does:** Opens a neat, organized data table utilizing the `ttk.Treeview` module. It displays all active products inside the warehouse—listing their product IDs, names, exact quantities, and unit rates side-by-side.

### 6. Customer Accounting Matrix
* **File Asset:** `cus.png`
* **What it does:** Dedicated tracking area for customer accounts. It records necessary details like credit loops, debit logs, and phone numbers to keep customer ledgers accurate and properly balanced.

### 7. Customer Details Ledger
* **File Asset:** `prfl.png`
* **What it does:** Pulls a clean spreadsheet view containing all registered customer records from the MySQL database, allowing shop managers to search balance frameworks quickly.

### 8. Broker Profiles & Transactions
* **File Asset:** `bro.png`
* **What it does:** A specialized tracking system for middle-men and supply brokers. It manages separate debit and credit records for third-party operations, preventing balance data overlaps with regular customers.

### 9. History Audit Logs
* **File Asset:** `his.png`
* **What it does:** The global system history viewer. It displays past logs of exactly what items were added, changed, or deleted over time, providing security tracking for stock and billing logs.

---

## 🛠️ Technical Stack

* **Frontend GUI:** Python Tkinter & TTK Themes
* **Database Backend:** MySQL (Relational Database)
* **Libraries Used:** `mysql.connector`, `tkcalendar`, `threading`

---

## 🚀 How to Run the Project Locally

### 1. Install Dependencies
Make sure you have Python installed, then run this command in your terminal:

<img width="2481" height="1754" alt="uzair project pdf_page-0001" src="https://github.com/user-attachments/assets/d86de71d-86fe-42a3-a326-f145a859a862" />



