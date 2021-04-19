
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
