FROM debian:latest
EXPOSE 5000
RUN apt-get update && apt-get install -y python3-pip && apt-get install sudo -y&& apt-get install git -y && apt-get install systemd -y && apt-get install libpcre3 -y && apt-get install nginx -y && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /home/Python
RUN git clone https://github.com/Krizsan0596/PySudoku.git
WORKDIR /home/Python/PySudoku
RUN pip3 install -r requirements.txt
RUN pip3 install uwsgi
RUN mv pysudoku.service /etc/systemd/system/pysudoku.service
RUN mv pysudoku /etc/nginx/sites-available/pysudoku
RUN sudo ln -s /etc/nginx/sites-available/ /etc/nginx/sites-available/pysudoku
RUN sudo unlink sudo unlink /etc/nginx/sites-enabled/default
RUN sudo systemctl enable pysudoku
RUN sudo systemctl enable nginx
ENTRYPOINT ["uwsgi", "--master", "-p", "4", "-w", "main:app", "--protocol=http", "--thunder-lock", "--socket", "0.0.0.0:5000"]