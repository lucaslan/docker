FROM centos

RUN yum -y install python python-devel python-setuptools flask epel-release  && yum install -y python-pip && \
 pip install cherrypy flask && mkdir -p /app && yum clean all

ADD . /app

EXPOSE 80

CMD ["python", "/app/server.py"]