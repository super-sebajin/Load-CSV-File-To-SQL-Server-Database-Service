#!/bin/bash
#we need to wait for SQL Server to initialize completely.
sleep 30s

/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P Your_Strong@Password1 -d master -i init.sql
