FROM  python:3.13-slim


WORKDIR /app

RUN pip install pipenv
COPY ["Pipfile", "Pipfile.lock", "./"]
RUN pipenv install --system --deploy
COPY ["predict.py", "model.pkl", "./"]
RUN pip install --no-cache-dir waitress
EXPOSE 9696
ENTRYPOINT ["python", "-m", "waitress.server", "predict:app", "--host", "0.0.0.0", "--port", "9696"]

