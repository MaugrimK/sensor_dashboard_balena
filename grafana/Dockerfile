FROM balenalib/raspberry-pi:buster

RUN install_packages \
      fontconfig-config \
      fonts-dejavu-core \
      libfontconfig1 \
      ucf \
      jq \
      wget

RUN /bin/bash -c "wget -q -O /tmp/grafana.deb https://dl.grafana.com/oss/release/grafana-rpi_6.3.6_armhf.deb"

RUN dpkg -i /tmp/grafana.deb && rm /tmp/grafana.deb

COPY ./grafana.ini /usr/share/grafana/conf/custom.ini
COPY ./provisioning /usr/src/app/provisioning
COPY ./*.sh /usr/src/app/
RUN chmod +x /usr/src/app/*.sh

CMD ["/bin/sh","/usr/src/app/entry.sh"]