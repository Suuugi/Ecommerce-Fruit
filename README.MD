git clone https://github.com/Suuugi/Ecommerce-Fruit.git ecommerce
cd ecommerce
py -m venv venv
Set-ExecutionPolicy Unrestricted -Scope Process
./venv/Scripts/activate.ps1
pip install -r requirements.txt
py manage.py makemigrations accounts
py manage.py makemigrations store
py manage.py migrate
py manage.py runserver