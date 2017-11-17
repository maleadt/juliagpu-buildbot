FROM       python:3-stretch
MAINTAINER tim.besard@gmail.com

RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
                    # basic stuff
                    build-essential ca-certificates \
                    # Julia
                    cmake curl gfortran git m4 python \
                    # master.cfg
                    rsync clang ccache && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/local/lib/ccache/bin && \
    ln -s /usr/bin/ccache /usr/local/lib/ccache/bin/clang && \
    ln -s /usr/bin/ccache /usr/local/lib/ccache/bin/clang++ && \
    ln -s /usr/bin/ccache /usr/local/lib/ccache/bin/gfortran
ENV CCACHE_DIR /cache/ccache

RUN pip --no-cache-dir install buildbot-worker==0.9.13

WORKDIR "/var/lib/buildbot"
COPY . .

VOLUME ["/data", "/cache"]

CMD ["twistd", "-ny", "buildbot.tac"]
