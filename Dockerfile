FROM python:3.9.5
RUN apt update
RUN apt -y install python3-pip
RUN pip install Flask
RUN git clone https://github.com/niggiover9000/EaglegangDashboard
WORKDIR EaglegangDashboard
CMD ["python", "main.py"]
EXPOSE 5000
