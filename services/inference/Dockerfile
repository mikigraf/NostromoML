FROM golang:1.19.3

WORKDIR /app

COPY go.mod .
COPY go.sum .
RUN go mod download

COPY ./cmd/*.go .

RUN go build -o /inference

EXPOSE 8084

CMD [ "/inference" ]