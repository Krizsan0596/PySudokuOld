FROM debian:latest
EXPOSE 5000
RUN apt-get update && apt-get install -y python3-pip && apt-get install git -y && apt-get install -y systemd && apt-get install libpcre3 -y && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /home/Python
RUN git clone https://github.com/Krizsan0596/PySudoku.git
WORKDIR /home/Python/PySudoku
RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi
RUN cp pysudoku.service /etc/systemd/system/pysudoku.service
ENTRYPOINT ["uwsgi", "--master", "-p", "4", "-w", "main:app", "--protocol=http", "--thunder-lock", "--socket", "0.0.0.0:5000"]