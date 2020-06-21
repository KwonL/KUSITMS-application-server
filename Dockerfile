FROM python:3.8.3

LABEL maintainer="lkh116@snu.ac.kr"

WORKDIR /root

ADD server/requirements.txt .
RUN pip install -r requirements.txt

ADD . .

WORKDIR /root/server

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-", "wsgi:application"]