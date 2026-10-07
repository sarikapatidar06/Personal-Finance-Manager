# Personal Finance Manager - Project Documentation

## 1. Project Overview

Personal Finance Manager is a Python-based command-line application designed to help users record, manage, search, and analyze their daily expenses.

The application provides a simple and user-friendly interface for maintaining financial records and generating useful expense reports.

## 2. Objectives

The main objectives of this project are:

- To record daily expenses.
- To store expense data permanently using CSV files.
- To provide expense search functionality.
- To generate total and average expense reports.
- To provide category-wise expense analysis.
- To generate monthly expense reports.
- To provide backup functionality.
- To validate user inputs and handle errors.
- To demonstrate Object-Oriented Programming in Python.

## 3. Technologies Used

- Python 3
- CSV File Handling
- Object-Oriented Programming (OOP)
- Unittest
- Command Line Interface (CLI)

## 4. Project Features

### Add New Expense

Users can add an expense by entering:

- Amount
- Category
- Date
- Description

### View All Expenses

Users can view all saved expenses in the application.

### Expense Report

The application calculates:

- Total expenses
- Average expense
- Category-wise expense summary

### Search Expense

Users can search expenses using a category or description keyword.

### Monthly Report

Users can enter a month in `YYYY-MM` format and view:

- Total expenses for that month
- Number of expenses

### Backup Expenses

The application creates a backup copy of the expense CSV file.

### Data Persistence

Expense records are stored in:

`data/expenses.csv`

Backup data is stored in:

`data/expenses_backup.csv`

## 5. Project Structure

```text
Personal-Finance-Manager/
│
├── data/
│   ├── expenses.csv
│   └── expenses_backup.csv
│
├── docs/
│   ├── PROJECT_DOCUMENTATION.md
│   └── user_guide.md
│
├── screenshots/
│
├── src/
│   ├── expense.py
│   ├── file_manager.py
│   ├── menu.py
│   ├── reports.py
│   └── utils.py
│
├── tests/
│   └── test_finance_manager.py
│
├── main.py
├── README.md
└── requirements.txt
