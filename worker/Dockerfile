FROM       buildbot/buildbot-worker:v0.9.12.post1
MAINTAINER tim.besard@gmail.com

USER root

RUN apt-get update && \
    apt-get install --yes --no-install-recommends \
                    # basic stuff
                    build-essential ca-certificates \
                    # Julia
                    cmake curl gfortran git m4 python \
                    # master.cfg
                    clang ccache && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /usr/local/lib/ccache/bin && \
    ln -s /usr/bin/ccache /usr/local/lib/ccache/bin/clang && \
    ln -s /usr/bin/ccache /usr/local/lib/ccache/bin/clang++ && \
    ln -s /usr/bin/ccache /usr/local/lib/ccache/bin/gfortran
ENV CCACHE_DIR /cache/ccache

# NOTE: keep in sync with upstream Dockerfile
USER buildbot

VOLUME ["/data", "/cache"]
