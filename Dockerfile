FROM python:3.8.3

LABEL maintainer="lkh116@snu.ac.kr"

RUN apt update && \
    apt install -y locales && \
    sed -i -e 's/# ko_KR.UTF-8 UTF-8/ko_KR.UTF-8 UTF-8/' /etc/locale.gen && \
    dpkg-reconfigure --frontend=noninteractive locales

WORKDIR /root

ADD server/requirements.txt .
RUN pip install -r requirements.txt

ADD . .

WORKDIR /root/server

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-", "wsgi:application"]