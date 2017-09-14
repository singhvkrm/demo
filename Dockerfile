 From centos:7
 RUN yum install -y python bash curl net-tools
 COPY server.py /server.py
 ENTRYPOINT ["python","/server.py"]
