FROM python:3.9.5
RUN apt update
RUN apt -y install python3-pip
RUN pip install Flask
RUN git clone https://github.com/niggiover9000/EaglegangDashboard
CMD ["python", "EaglegangDashboard/main.py"]
WORKDIR EaglegangDashboard
EXPOSE 5000
