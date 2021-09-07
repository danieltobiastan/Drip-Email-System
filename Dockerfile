# syntax=docker/dockerfile:1
FROM python:3.9.7-buster

# Set up to be able to run the echo commands
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

# Copy files from system directory to docker new directory and set it as curent working directory in docker
COPY . /Drip-Email-System
WORKDIR /Drip-Email-System

# Run these commands to set up SENDGRID
RUN echo "export SENDGRID_API_KEY='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'" > sendgrid.env
RUN echo "sendgrid.env" >> .gitignore
RUN source ./sendgrid.env

#Not sure if necessary
#RUN useradd -ms /bin/bash newuser
#USER newuser

# Install the requirements
RUN pip install -r requirements.txt

# Terminal command for the main program
CMD ["python", "drip.py"]