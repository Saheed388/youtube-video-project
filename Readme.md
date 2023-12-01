The first thing to do is to get your docker insatlled on your system

-- https://docs.docker.com/engine/install/

The next step is to get your mage running on dpcker

link -- https://docs.mage.ai/getting-started/setup
run this on your powershell
-- docker run -it -p 6789:6789 -v ${PWD}:/home/src mageai/mageai /app/run_app.sh mage start [project_name]

Next step 
set up psql and mysql also running on docker

create a folder name musql
 
For mysql copy the create a file name docker-compose.yml

 --version: '3.8'

services:
  mysql_db:
    image: mysql:8
    environment:
      - MYSQL_ROOT_PASSWORD=root
      - MYSQL_DATABASE=root
      - MYSQL_USER=root
      - MYSQL_PASSWORD=root
    volumes:
      - "./mysql_data:/var/lib/mysql:rw"
    ports:
      - "3307:3306"
    networks:
      - airflow_default  # Use the specified network

  phpmyadmin:
    image: phpmyadmin/phpmyadmin
    environment:
      - PMA_HOST=mysql_db
      - PMA_PORT=3306
      - MYSQL_ROOT_PASSWORD=root
    ports:
      - "84:80"
    depends_on:
      - mysql_db
    networks:
      - airflow_default  # Use the specified network
    volumes:
      - ./apache2.conf:/etc/apache2/conf-enabled/apache2.conf:ro

networks:
  airflow_default:  # Define the network
    external: true

For psql
create a folder name posrgesql
For psql copy the create a file name docker-compose.yml

-- services:
  postgres_db:
    image: postgres:13
    environment:
      - POSTGRES_USER=psql
      - POSTGRES_PASSWORD=psql
      - POSTGRES_DB=psql
    volumes:
      - "./nytaxi_postgres_data:/var/lib/postgresql/data:rw"
    ports:
      - "5432:5432"
    networks:
      - airflow
  pgadmin:

    image: dpage/pgadmin4
    environment:
     - PGADMIN_DEFAULT_EMAIL=prefared_mail@gmail.com
     - PGADMIN_DEFAULT_PASSWORD=prefared_password
    ports:
     - "82:80"
    volumes:
     - ./data_pgadmin:/var/lib/pgadmi
    networks:
      - airflow
networks:
  airflow:
    external:
      name: airflow_default

-- Navigate to your postgres and psql folder in your terminal
Then run 
-- docker-compose up -d

That will be created

Next Step 
the website we are scraping 

https://dev.socrata.com/docs/endpoints.html


Configure the Mage settings:
Prior to establishing connections with MySQL and PSQL, verify the existence of the "io_config.yaml" file. Look for the sections labeled MYSQL and PSQL, and ensure that you provide the necessary information.





