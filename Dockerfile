FROM python:3.12-slim as compiler
LABEL authors="dtrai2"

ENV PYTHONUNBUFFERED 1
WORKDIR /app/
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install -U shiny-invoice

FROM python:3.12-slim as runner
LABEL authors="dtrai2"

WORKDIR /app/
COPY --from=compiler /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . /app/
EXPOSE 8000
ENTRYPOINT ["shiny-invoice"]