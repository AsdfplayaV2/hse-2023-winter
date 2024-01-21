# Dockerfile-sqlite
FROM alpine:latest

# Install SQLite
RUN apk add --no-cache sqlite

# Copy your SQLite database file into the container
COPY tasklist.db /tasklist.db
