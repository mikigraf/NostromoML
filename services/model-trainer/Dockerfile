FROM golang:1.19.3

WORKDIR /app

COPY go.mod .
COPY go.sum .
RUN go mod download

COPY ./cmd/*.go .

RUN go build -o /model-trainer

EXPOSE 8082

CMD [ "/model-trainer" ]