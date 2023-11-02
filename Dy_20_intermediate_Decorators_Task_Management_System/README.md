Introduction
The Task Management System is a software application that allows users to manage their tasks and to-do lists. This document outlines the requirements for the development of the Task Management System.

2. Project Overview
The Task Management System will be a command-line application that allows users to create accounts, log in, add tasks, view tasks, and, if they have the admin role, delete tasks. The application will store user data and task information in data files.

3. Objectives
The primary objectives of the Task Management System are as follows:

Provide users with a platform to manage their tasks.
Implement user authentication and access control.
Store user data and task information securely.
4. Features
The key features of the Task Management System include:

User account creation
User login
Adding new tasks
Viewing tasks
Deleting tasks (admin role only)
5. User Roles
The system will support two user roles:

User: Can add and view tasks.
Admin: Can delete tasks in addition to the user features.
6. Functional Requirements
User Account Management
Users can create an account by providing a username and password.
Users can log in using their username and password.
User authentication is required to access the system.
Task Management
Users can add a task.
Users can view their tasks.
Admin users can delete tasks.
7. Non-Functional Requirements
Security: Passwords and sensitive information must be stored securely.
Data Persistence: User data and task information should be saved in data files.
User Interface: The system will be a command-line interface.
8. Data Storage
User data will be stored in a 'user_data.json' file.
Task data will be stored in a 'task_data.json' file.
9. Security
User passwords will be hashed before storage.
Data files will be protected to prevent unauthorized access.
10. User Interface
The application will provide a text-based, command-line interface for user interaction.