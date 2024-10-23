# Use the official Redis image from Docker Hub
FROM redis:latest

# Set the working directory (optional)
WORKDIR /data

# Expose the default Redis port
EXPOSE 6379

# Start Redis server with default configuration
CMD ["redis-server","--requirepass", "root", "--maxmemory", "256mb"]
