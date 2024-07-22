# Project: Load CSV FILE TO SQL SERVER

## Description
This is a 3-container project that performs an ETL job for the file `example.csv` that is included.

I divide this service into 3 containers to conserve separation of concern as much as possible. 

This project uses `docker-compose` to generate a `Microsoft SQL Server` Instance, and two linux containers that run `FastApi` applications. The two "Python containers" have a simple communication scheme using HTTP methods to 
"speak" to each other through the network provided by the `Docker` engine to send a file via HTTP and load it 
unto to the third container that contains the `Microsoft SQL Server` instance.

The project is fairly new, so it will lack in documentation, however to run all you need to is to execute `docker-compose` with the appropriate arguments. A simple `docker-compose up -d` should do the job.