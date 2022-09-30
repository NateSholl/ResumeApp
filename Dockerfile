FROM tiangolo/uwsgi-nginx-flask:python3.8-alpine
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /home/ubuntu/git/ResumeApp/app/static
COPY ./requirements.txt /home/ubuntu/git/ResumeApp/requirements.txt
RUN pip install -r /home/ubuntu/git/ResumeApp/requirements.txt
