FROM ubuntu:16.04

MAINTAINER GeenStack <hayleytops@gmail.com>

RUN apt-get update && \
	apt-get -y install sudo &&\
	apt-get -y install nano &&\
	apt-get -y install python3

RUN mkdir /bin/scripts
COPY ./script.py /bin/scripts/
RUN chmod 747 /bin/scripts/script.py

#	Add user without root privileges 
#	and set home directory to him
RUN useradd -ms /bin/bash escalator
RUN echo 'escalator ALL=(root) NOPASSWD:/bin/scripts/script.py' >> /etc/sudoers
USER escalator
WORKDIR /home/escalator
