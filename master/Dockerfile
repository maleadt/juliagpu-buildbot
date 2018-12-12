FROM       python:3-stretch
MAINTAINER tim.besard@gmail.com

RUN pip --no-cache-dir install buildbot[bundle]==1.1.1 \
                               buildbot_travis==0.6.3 \
                               txrequests==0.9.6

WORKDIR "/var/lib/buildbot"
COPY . .

VOLUME ["/config", "/data"]

CMD ["./start.sh"]
