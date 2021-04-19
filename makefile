
dbstatus:
	systemctl status postgresql

dbstop: 
	systemctl stop postgresql

dbstart: 
	systemctl start postgresql

start:
	python3 test.py

db:
	psql -U musa -d gmessengerdb

install_packages:
	pip install -r requirements.txt


refresh_db:
	./drop_tables.sh
	./create_tables.bash


fill_db:
	./fill_tables.bash

