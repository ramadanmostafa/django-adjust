FROM python:3.6
WORKDIR /code
RUN apt-get -y update \
    && apt-get install -y default-mysql-client python-cffi libcairo2 libpango1.0-0 libgdk-pixbuf2.0-0 shared-mime-info libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libffi-dev \
    && apt-get -y clean
RUN apt-get update && apt-get install -y gettext
ADD ./requirements.txt /code/requirements.txt
RUN pip install --upgrade setuptools wheel
RUN pip install -r requirements.txt