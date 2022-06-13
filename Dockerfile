FROM python:3.8
WORKDIR /app/django

ENV PYTHONIOENCODING=utf-8

RUN python -m pip install --upgrade pip >/dev/null 2>&1
COPY requirements.txt ./
RUN pip install -r requirements.txt >/dev/null 2>&1
COPY . .

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD python3 manage.py migrate && \
python3 manage.py runserver 0:8000

EXPOSE 8000


# FROM python:3.8

# WORKDIR /usr/src/app

# COPY . .

# ENV PYTHONIOENCODING=utf-8

# WORKDIR ./python_django_blogapp_restframework
# RUN pip install -r requirements.txt
#CMD ["python3", "manage.py", "migrate"]
#CMD ["python3", "manage.py", "runserver", "0:8000"]

# CMD python3 manage.py migrate && \
# python3 manage.py runserver 0:8000

# EXPOSE 8000