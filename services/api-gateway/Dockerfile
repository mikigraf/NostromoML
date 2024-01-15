FROM golang:1.19.3

WORKDIR /app

COPY ../../pkg ./services/
RUN go mod download


RUN go build -o /api-gateway ./cmd/main.go

EXPOSE 8085

CMD [ "/api-gateway" ]