FROM python:3.8
WORKDIR /app
COPY requirements.txt /app
RUN python -m venv /app/env && \
  /app/env/bin/pip install -r requirements.txt
ENV PATH="/app/env/bin:$PATH"
COPY . /app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
