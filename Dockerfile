FROM python:3.4-alpine
COPY ./myproject /code
WORKDIR /code
CMD ["python3", "-m", "http.server", "--bind", "0.0.0.0", "--cgi", "8000"]
