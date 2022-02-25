FROM python:3.6
RUN pip install Flask
RUN useradd -ms /bin/bash admin \
    && mkdir sounds

RUN apt-get update -y

RUN apt-get install mpg123 -y
RUN apt-get install wget -y
RUN apt install pulseaudio -y



USER admin
WORKDIR /app
COPY app /app
CMD ["python", "app.py"]