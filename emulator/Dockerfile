# Based on https://github.com/nickstenning/docker-slapd/blob/master/Dockerfile

FROM phusion/baseimage:focal-1.0.0

ENV HOME /root

# Disable SSH
RUN rm -rf /etc/service/sshd /etc/my_init.d/00_regen_ssh_host_keys.sh

# Use baseimage-docker's init system.
CMD ["/sbin/my_init"]

# Configure apt
RUN apt-get -y update

# Install slapd
RUN LC_ALL=C DEBIAN_FRONTEND=noninteractive apt-get install -y slapd

EXPOSE 389

ADD slapd.sh /etc/service/slapd/run
RUN chmod +x /etc/service/slapd/run

COPY schema /root/schema
COPY slapd.conf.dist /root
COPY build_config.py /root

RUN python3 /root/build_config.py

RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
