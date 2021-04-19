#! /usr/bin/bash

psql -d gmessengerdb -c "insert into users (login, name, avatar, online) values 
('logmusa', 'musa', '', TRUE),
('log1', 'name1', '', FALSE),
('log2', 'name2', '', TRUE),
('log3', 'name3', '', TRUE),
('log4', 'name4', '', FALSE),
('log5', 'name5', '', TRUE),
('log6', 'name6', '', FALSE),
('log7', 'name7', '', TRUE),
('log8', 'name8', '', FALSE)
"


psql -d gmessengerdb -c "insert into dialogs (dialog_id, type, avatar) values 
(1, 'p2p', ''),
(2, 'dialog', ''),
(3, 'dialog', ''),
(4, 'p2p', ''),
(5, 'dialog', ''),
(6, 'p2p', '')
"


psql -d gmessengerdb -c "insert into dialogs_info (dialog_id, user_id) values 
(1, 1),
(1, 2),
(2, 1),
(2, 2),
(2, 3),
(3, 3),
(3, 4),
(3, 5),
(4, 6),
(4, 7),
(5, 8),
(5, 9),
(5, 3),
(6, 6),
(6, 9)
"

psql -d gmessengerdb -c "insert into messages (dialog_id, user_id, msg, picture, status) values 
(1, 1, 'it is from me', '', TRUE),
(1, 2, 'this message', '', FALSE),
(2, 3, 'this message', '', FALSE),
(3, 3, 'good, broo', '', FALSE),
(4, 6, 'i want to do something', '', TRUE),
(5, 3, 'how does it work?', '', TRUE),
(6, 9, 'let a = 2;', '', FALSE)
"