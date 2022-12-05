FROM python:3.8.5-alpine
RUN apk update && apk upgrade && apk add --no-cache libffi-dev
COPY . /app
WORKDIR /app
ENV CRYPTOGRAPHY_DONT_BUILD_RUST=1
RUN apk add gcc musl-dev python3-dev libressl-dev cargo rust
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["rest.py"]