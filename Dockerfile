FROM python:3.10-bullseye
RUN mkdir "/docker_app"
WORKDIR "/docker_app"
COPY ".env.docker" ".env"
COPY . .
RUN pip install -r requirements.txt
ENV PYTHONUNBUFFERED 1
ARG HTTP_PORT
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "HTTP_PORT"]