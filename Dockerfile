FROM alpine:latest
RUN apk add --no-cache ffmpeg
ENTRYPOINT [ "ffmpeg" ]