FROM debian:stretch

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -qy procps htop psmisc dfc ncdu tcpdump && apt-get clean

CMD [ "/bin/bash" ]



