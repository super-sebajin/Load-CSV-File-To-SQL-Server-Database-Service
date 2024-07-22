#!/bin/bash


#this will run as a background process
/run-initialization.sh &

#and this will be executed, the idea is to wait for the server to come up first
/opt/mssql/bin/sqlservr

