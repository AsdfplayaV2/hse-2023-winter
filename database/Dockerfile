# Use the official PostgreSQL image from Docker Hub
FROM postgres:latest

# Set the PostgreSQL user and password environment variables
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword
ENV POSTGRES_DB=mydatabase

# Copy the modified SQL initialization script to the container
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL default port
EXPOSE 5432
