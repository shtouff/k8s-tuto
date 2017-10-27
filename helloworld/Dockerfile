FROM debian:stretch
ENV FLASK_APP helloworld.py
ENV FLASK_DEBUG 1
ENV DEBIAN_FRONTEND non-interactive
ADD ./src/ /opt/helloworld/
RUN apt-get update && apt-get install -y python3-venv && cd /opt/helloworld && python3 -mvenv . && /opt/helloworld/bin/pip install wheel && /opt/helloworld/bin/pip install -r /opt/helloworld/requirements.txt
WORKDIR /opt/helloworld
ENTRYPOINT [ "/opt/helloworld/bin/flask",  "run" ]
