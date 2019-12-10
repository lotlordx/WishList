#official Python runtime as a parent image
FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /wishlist_service

WORKDIR /wishlist_service

ADD . /wishlist_service/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt