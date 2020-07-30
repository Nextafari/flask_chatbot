# Inheriting from already existing docker image
FROM python:3.6


# Creating an env
ENV PYTHONUNBUFFERED 1


# Create new folder in container
RUN mkdir /flask_chatbot


# Make directory working directory
WORKDIR /flask_chatbot

# Copy the code from main directory to the container repo
COPY . /flask_chatbot/


# Install pip requirements in container
RUN pip3 install -r requirements.txt

# # Assigning a port to the app
# EXPOSE 8000


# Calls the app to run it 
CMD [ "python", "bot_app.py" ]
