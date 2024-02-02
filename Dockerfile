####################################
############ OPEN AGENT ############
###### BY ATTUNE ENGINEERING #######
####################################

FROM gitpod/workspace-python-3.9:latest

### SET ENVIRONMENT
USER root
RUN mkdir -p /workspace/open-agent/
RUN chown -R gitpod:gitpod /workspace/open-agent/
WORKDIR /workspace/open-agent/

### INSTALL DEPENDENCIES
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    wget \
    cowsay \
    && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/*

### COPY CONTENTS
COPY . /workspace/open-agent/

### INSTALL LIBRARIES
USER gitpod
RUN pip install --upgrade pip && \
    python3 -m pip install -U -r /workspace/open-agent/requirements.txt && \
    rm /workspace/open-agent/requirements.txt

ENTRYPOINT ["/workspace/open-agent/bin/docker_entry.sh"]

########################

