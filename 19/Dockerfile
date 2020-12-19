FROM ubuntu:21.04
CMD ["curl", "http://10.13.0.26:8000/test"]
EXPOSE 80
RUN groupadd -g 999 appuser && \
    useradd -r -u 999 -g appuser appuser
USER appuser