# EXPENSE TRACKER

A simple web based application to track your expenses. 
<br/>
Made with Django and Bootstrap.

## Installation

1. Clone the repository
   ```
        git clone https://github.com/rishav-jha-mech/Expense-Tracker.git
   ```
2. Activate virtual environment
    ```
        pip install virtualenv
        virtualenv env
        cd env/Scripts
        activate
    ```
3. Install requirements - run this command on the root directory of the project
    ```
        pip install -r requirements.txt
    ```  
4. Run the project
    ```
        python manage.py migrate
        python manage.py runserver
    ```