# password_manager

Simple little password manager that usilizes PostgreSQL

User navigates the menu through the command line through a simple text menu.

The script allows user first to connect to the PostgreSQL database with a password.

Then the user is prompted to select if they want to retrieve login information for an application or if they want to create and store a new login information.

Requirements:

1) User must install the following exernal python libraries: "psycopg2", "pyperclip", "random-password-generator"
2) User must install and initiate a postgres server with login information onto their device.
3) User must create database with a name that matches the database variable in the script
