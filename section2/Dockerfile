# Use the official PostgreSQL image as the base image
FROM postgres:latest

# Set environment variables for PostgreSQL
ENV POSTGRES_USER postgres
ENV POSTGRES_PASSWORD password
ENV POSTGRES_DB postgresdb

# Execute SQL DDL commands to create tables
COPY *.sql /docker-entrypoint-initdb.d/

# Expose the PostgreSQL port
EXPOSE 5432

# Run the PostgreSQL server
CMD ["postgres"]