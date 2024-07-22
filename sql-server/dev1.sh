#!/bin/bash

# make back up

query_result=$(/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P Your_Strong@Password1 -d APP_DATA -Q "select * from [RAW_DATA].[INTENSITY_APP_FILE];" )

cat "$query_result"
