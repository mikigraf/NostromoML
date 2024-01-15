FROM golang:1.19.3

WORKDIR /app

COPY ../../pkg ./services/
COPY go.mod .
COPY go.sum .
RUN go mod download

COPY ./cmd/*.go .

RUN go build -o /model-metadata

EXPOSE 8083

CMD [ "/model-metadata" ]