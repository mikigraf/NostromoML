FROM golang:1.19.3

WORKDIR /app

COPY ../../pkg ./services/
COPY go.mod .
COPY go.sum .
RUN go mod download

COPY ./cmd/*.go .

RUN go build -o /training-scheduler

EXPOSE 8081

CMD [ "./training-scheduler" ]
