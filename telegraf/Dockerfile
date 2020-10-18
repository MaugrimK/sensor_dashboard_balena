FROM balenalib/raspberry-pi:buster

RUN install_packages wget

RUN /bin/bash -c "wget -q -O /tmp/telegraf.deb https://dl.influxdata.com/telegraf/releases/telegraf_1.12.2-1_armhf.deb"

RUN dpkg -i /tmp/telegraf.deb && rm /tmp/telegraf.deb

COPY telegraf.conf /etc/telegraf/telegraf.conf

CMD telegraf