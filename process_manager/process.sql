#process 创建
"""
create table process(
item int primary key auto_increment,
region varchar(10) not null,
line varchar(20) not null,
groupmark varchar(30) not null,
stationcode varchar(50) not null,
stationname varchar(80) not null,
retestrate float not null default 0.0 ,
linedownrate float not null default 0.0,
efficiency decimal(3,2) not null default 0.92,
manualct float not null,
machinect float not null,
stationct float,
piece int not null default 1,
uphperhc int not null,
uphpermachine int,
hcpermachine int not null default 1,
hc float,
qpl float,
targetuph int not null,
machinetype varchar(30),
remark text);
"""