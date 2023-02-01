FROM python:3.10

COPY . /ctf
WORKDIR /ctf

# install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# define the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./run.py"]
