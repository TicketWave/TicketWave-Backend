FROM python:3.10

ENV PYTHONUNBUFFERED=1

WORKDIR "/app/backend"

COPY requirement.txt .

RUN pip install -r requirement.txt

COPY ./Ticketwave .

#RUN cd Ticketwave

#EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
