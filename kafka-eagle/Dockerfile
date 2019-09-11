FROM java:8-alpine

ENV KE_HOME=/opt/kafka-eagle
ENV EAGLE_VERSION=1.3.9

RUN apk --update add wget gettext tar bash sqlite

#get and unpack kafka eagle
RUN mkdir -p /opt/kafka-eagle/conf;cd /opt && \
    wget https://github.com/smartloli/kafka-eagle-bin/archive/v${EAGLE_VERSION}.tar.gz && \
    tar zxvf v${EAGLE_VERSION}.tar.gz -C kafka-eagle --strip-components 1 && \
    cd kafka-eagle;tar zxvf kafka-eagle-web-${EAGLE_VERSION}-bin.tar.gz --strip-components 1 && \
    chmod +x /opt/kafka-eagle/bin/ke.sh && \
    mkdir -p /hadoop/kafka-eagle/db

ADD entrypoint.sh ${KE_HOME}/entrypoint.sh
COPY system-config.properties ${KE_HOME}/conf/system-config.properties

EXPOSE 8048 8080

WORKDIR /opt/kafka-eagle

ENTRYPOINT ["sh", "entrypoint.sh"]