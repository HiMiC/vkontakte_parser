# Pull base image
FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
RUN mkdir /code

WORKDIR /code
ADD ./code/requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

RUN apt update
RUN apt -y upgrade
RUN apt install -y bash libmariadbclient-dev-compat mariadb-client python3-dev
RUN apt install -y
RUN pip install mysqlclient
RUN pip install -r requirements.txt
RUN   apt-get clean && \
  rm -rf /tmp/* /var/lib/apt/lists/* /var/tmp/*;

# Copy project
#COPY ./code/ /code/

EXPOSE 8000

# docker build -t mysqltest2 .
# docker run -d -it -p 0.0.0.0:8000:8000 --name=kz2 mysqltest2
# docker exec -it kz2 bash
#
#DELETE
# docker stop kz2
# docker rm kz2
# docker rmi mysqltest2