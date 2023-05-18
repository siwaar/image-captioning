FROM python:3.9

COPY ./requirements.txt ./requirements.txt
COPY image_captioning image_captioning

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y
RUN pip install -r requirements.txt

CMD ["python3", "-m", "image_captioning.src.main"]