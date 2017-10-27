FROM shtouff/debian:stretch

ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8
ENV FLASK_APP helloworld.py
ENV FLASK_DEBUG 1

ADD src/ /opt/helloworld/

WORKDIR /opt/helloworld

RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -qy python3-venv && apt-get clean && python3 -mvenv . && bin/pip install wheel && bin/pip install -r requirements.txt

CMD [ "/opt/helloworld/bin/flask", "run", "-h", "0.0.0.0" ]
