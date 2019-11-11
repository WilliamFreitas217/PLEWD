FROM mysql
ENV MYSQL_DATABASE plewd
COPY ./sql-scripts/ /docker-entrypoint-initdb.d/
