FROM ubuntu:16.04

RUN apt-get update -y && apt-get install -y \
    python-pip \
    python-dev \
    python-lxml \
    build-essential \
    qt5-default \
    libqt5webkit5-dev \
    xvfb \
    git


RUN pip install --upgrade pip && pip install \
    lxml \
    xvfbwrapper \
    bs4 \
    dryscrape \
    awscli \
    Babel \
    bcdoc \
    BeautifulSoup \
    beautifulsoup4 \
    boto \
    botocore \
    cffi \
    characteristic \
    colorama \
    cryptography \
    cssselect \
    dnspython \
    docutils \
    enum34 \
    eventlet \
    greenlet \
    html5lib \
    incapsula-cracker \
    Jinja2 \
    jmespath \
    json2html \
    lxml \
    MarkupSafe \
    mechanize \
    monotonic \
    MonthDelta \
    ndg-httpsclient \
    nested-lookup \
    nose \
    parsel \
    Pillow \
    pip \
    pyasn1 \
    pyasn1-modules \
    pycparser \
    PyDispatcher \
    Pygments \
    pymongo \
    pyocr \
    pyOpenSSL \
    pytesseract \
    python-dateutil \
    python-magic \
    PyYAML \
    queuelib \
    requests \
    rsa \
    Scrapy===1.5.0\
    seafileapi \
    service-identity \
    setuptools \
    simplejson \
    six \
    Sphinx \
    SQLAlchemy \
    Twisted \
    unicode \
    Unidecode \
    urllib3 \
    virtualenv \
    w3lib \
    webencodings \
    webkit-server \
    Werkzeug \
    xvfbwrapper \
    zope.interface

ADD xvfb.init /etc/init.d/xvfb
RUN chmod +x /etc/init.d/xvfb


# copy all files to /app
COPY . /app

# change working directory to /app
WORKDIR /app

# expose port
#EXPOSE 5000

# run python
#ENTRYPOINT [""]
ENTRYPOINT ["./launch.init"]

ENV AM_I_IN_A_DOCKER_CONTAINER Yes

ENV MONGO_HOST "host.docker.internal"

RUN chmod +x /app/launch.init

# run app
#CMD (service xvfb start; export DISPLAY=:10; python get_dc_data.py)

