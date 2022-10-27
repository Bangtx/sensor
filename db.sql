create table sensor (
	id bigint NOT NULL IDENTITY PRIMARY KEY,
	name text,
	host text,
	port int,
	unit int,
	position text,
);


create table casting_machine (
	id bigint NOT NULL IDENTITY PRIMARY KEY,
	name text,
	datetime datetime default CURRENT_TIMESTAMP
);


create table temperature (
	id bigint NOT NULL IDENTITY PRIMARY KEY,
	temp int,
	sensor_id bigint FOREIGN KEY REFERENCES sensor(id),
	status int,
	casting_machine_id bigint FOREIGN KEY REFERENCES casting_machine(id),
	datetime datetime default CURRENT_TIMESTAMP
);


insert into casting_machine (name) values ('may 1');


insert into sensor (name, host, port ,unit)
values ('sensor 1', '192.168.1.254', 8880, 1),
       ('sensor 2', '192.168.1.254', 8880, 2)