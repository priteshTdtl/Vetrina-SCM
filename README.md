# Vetrina-SCM
## Initial steps to follow :
### 1. Clone this repo in your VS code.
#### - ***Don't work directly on `main` branch.***
#### - ***Create your `new branch` where you will work.***
#### - ***Verify your branch before you make any changes in the code.***

#### - ***Run phpmyadmin and create DB named ```baapgpt_db```***
#### - ***Import `users.sql` table present in parent folder of BAAPGPT to your phpmyadmin's `baapgpt_db`***
### 2. Open terminal and run following commands:
```bash
1. cd Backend/Backendproject
2. python manage.py makemigrations
3. python manage.py migrate
```

### 3. In `Backendproject` dir install packages:
```bash
1. pip install django
2. python -m pip install django-cors-headers
3. pip install mysqlclient
```
### 4. Run django server in `Backendproject` dir :
```bash
python manage.py runserver
```
### 5. Open new terminal and :
```bash
cd Frontend
```

#### -`Inside Frontend directory` : _Install `npm` packages such as bootstrap, axios, react-router-dom, bcrypt, react and other necessary packages as per requirements_
#### -_Run the react server by following command in `Frontend` directory_
```bash
npm start
```
### 6. Redirect to ```http://localhost:3000``` in your browser
