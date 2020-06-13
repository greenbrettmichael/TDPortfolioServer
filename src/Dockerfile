FROM python:3.7-alpine

RUN apk --no-cache add \
                       # numpy dependency
                       g++  \
                       # Pillow dependencies
                       jpeg-dev \
                       zlib-dev \
                       freetype-dev \
                       lcms2-dev \
                       openjpeg-dev \
                       tiff-dev \
                       tk-dev \
                       tcl-dev \
                       harfbuzz-dev \
                       fribidi-dev
# TODO pre-compile numpy, Pillow, and Pandas which are not included in alpine
COPY requirements.txt /
RUN pip install --no-cache-dir -r /requirements.txt
COPY . /app
WORKDIR /app

ENTRYPOINT ["python"]
CMD ["app.py"]