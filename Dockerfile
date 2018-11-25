FROM python:3.7-alpine

WORKDIR /dlg

# Dependencies. They do not change so often
COPY Pipfile* /dlg/
RUN pip install pipenv && \
    pipenv install --system --deploy && \
    pip uninstall -y pipenv virtualenv virtualenv_clone

# App and deployment
COPY app /dlg/app/
COPY hypercorn.toml serve.py /dlg/
CMD ["hypercorn", "-c", "hypercorn.toml", "serve.py:dlg"]
EXPOSE 5000