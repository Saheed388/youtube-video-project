
install python
-- sudo apt-get update
sudo apt-get install update 


sudo apt-get install python3-apt

install wget
sudo apt-get install wget
wget https://bootstrap.pypa.io/get-pip.py 

install
sudo python3 get-pip.py

install
sudo apt-get install python3-pip
sudo apt-get install sqlite3

sudo apt install python3-venv

sudo apt-get install libpq-dev

python3 -m venv venv

source venv/bin/activate


pip install "apache-airflow[postgres]==2.5.0" --constraint "https://raw.githubusercontent.com/apache/airflow/constraints-2.5.0/constraints-3.7.txt"

airflow db init

install postgres
sudo apt-get install postgresql postgresql-contrib

sudo -i -u postgres

run this to connect to database

-- psql

CREATE DATABASE airflow;
CREATE USER airflow WITH PASSWORD 'airflow';
GRANT ALL PRIVILEGES ON DATABASE airflow TO airflow;

to exit the psql interface
\q
logout

To change from sqlite to postgresql

sed -i 's#sqlite:////home/ubuntu/airflow/airflow.db#postgresql+psycopg2://airflow:airflow@localhost/airflow#g' airflow.cfg

--To check connection
grep sql_alchemy airflow.cfg
--To check the executor
grep executor airflow.cfg


sed -i 's#SequentialExecutor#LocalExecutor#g' airflow.cfg
change back
sed -i 's#LocalExecutor#SequentialExecutor#g' airflow.cfg


airflow db init

airflow users create -u airflow -f airflow -l airflow -r Admin -e airflow@gmail.com

airflow webserver &



airflow scheduler

when returning version upgrade error
pip install --upgrade typing-extensions
