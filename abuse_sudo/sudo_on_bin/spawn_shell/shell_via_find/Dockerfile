FROM ubuntu:16.04

MAINTAINER GeenStack <hayleytops@gmail.com>

RUN apt-get update && \
	apt-get -y install sudo


#	Add user without root privileges 
#	and set home directory to him
RUN useradd -ms /bin/bash escalator
RUN echo 'escalator ALL=(root) NOPASSWD: /usr/bin/find' >> /etc/sudoers
USER escalator
WORKDIR /home/escalator
