FROM python:3.10

RUN apt-get update -yqq \
    && apt-get upgrade -yqq \
    && apt-get install --no-install-recommends -y sudo \
    && groupadd -g 1000 docker \
    && useradd -m -u 1000 -g docker docker -G sudo \
    && echo 'docker:docker' | chpasswd \
    #
    && apt-get autoremove -y \
    && apt-get autoclean -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

ADD . /mozio
WORKDIR /mozio

RUN pip install -r requirements.txt

USER docker