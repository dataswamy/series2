FROM continuumio/anaconda3
COPY . /PycharmProjects/series1/
EXPOSE 5000
WORKDIR  /PycharmProjects/series1/
RUN pip install -r requirements.txt
CMD python app.py

