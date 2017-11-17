FROM       python:3-jessie
MAINTAINER tim.besard@gmail.com

RUN pip --no-cache-dir install buildbot[bundle]==0.9.13 \
                               txrequests==0.9.5

WORKDIR "/var/lib/buildbot"
COPY . .

VOLUME ["/config", "/data", "/run/secrets"]

CMD ["./start.sh"]
