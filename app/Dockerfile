# Using Python 3.13.6 Alpine Image for minimum space used
FROM python:3.13.6-alpine3.22

# Adding a non-root user
RUN adduser -D echo
USER echo

# Setting /app as the working directory for the Docker image
WORKDIR /app

# Installing dependencies using requirements.txt file
COPY --chown=echo:echo requirements.txt .
RUN pip install --user --no-cache-dir -r requirements.txt

# Copying the entire directory to Docker image
COPY --chown=echo:echo . .

# Expose port 8000 and run the app
EXPOSE 8000 
CMD [ "python3", "app.py" ]