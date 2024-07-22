FROM mcr.microsoft.com/mssql/server:2022-preview-ubuntu-22.04 as service-sql-server-db

# Environment Variables
ENV ACCEPT_EULA=Y
ENV SA_PASSWORD=Your_Strong@Password1

COPY /sql-server .

# Expose SQL Server port
EXPOSE 1433

CMD /bin/bash ./entrypoint.sh


