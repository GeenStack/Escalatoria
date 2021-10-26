FROM ubuntu:16.04

MAINTAINER GeenStack <hayleytops@gmail.com>

RUN apt-get update && \
	apt-get -y install sudo &&\
	apt-get -y install nano

RUN mkdir /bin/scripts
COPY ./script.sh /bin/scripts/
RUN chmod 747 /bin/scripts/script.sh

#	Add user without root privileges 
#	and set home directory to him
RUN useradd -ms /bin/bash escalator
RUN echo 'escalator ALL=(root) NOPASSWD:/bin/scripts/script.sh' >> /etc/sudoers
USER escalator
WORKDIR /home/escalator
