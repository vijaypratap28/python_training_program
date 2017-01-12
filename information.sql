  create database acesspoint_database;
  use accesspoint_database;
  create table information
        (MACAddress varchar(50) not null,
         IPv4Address varchar(50), 
         IPv6Address varchar(50),
         Name varchar(20), 
         State varchar(20), 
         Tunnel varchar(20),
         Sec_Mode varchar(30),
         Mesh_Role varchar(20),
         PSK varchar(20),
         Timer varchar(50),
         HW_Version varchar(20),
         SW_Version varchar(20),
         Model varchar(20),
         Serial_number varchar(20), 
         PRIMARY KEY(MACAddress));

