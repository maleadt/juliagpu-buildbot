FROM       buildbot/buildbot-master:v0.9.12.post1
MAINTAINER tim.besard@gmail.com

RUN \
    pip install txrequests && \
    rm -r /root/.cache

RUN ln -s /config/master.cfg /var/lib/buildbot/

VOLUME ["/config", "/data", "/run/secrets"]
