# Use the basic Python 3 image as launching point
FROM ubuntu

# Fetch and Install python
RUN ["apt-get", "update"]
RUN ["apt-get", "install", "python","-y"]
RUN ["apt-get", "install","python-pip","-y"]
RUN ["apt-get", "install","python3-pip","-y"]

RUN ["pip3", "install", "bs4"]
RUN ["pip3", "install", "lxml"]
CMD ["pip3", "install", "bs4"]
CMD ["pip3", "install", "lxml"]
CMD ["pip3", "install", "urllib3"]
RUN ["pip3", "install", "boto"]

# Add the script, argv input syntax, & requirements to the Dockerfile
ADD eda_log.py /home

# ADD requirements.txt /home
# RUN ["pip","install","-r","./home/requirements.txt"]

# Execute the script
# CMD ["python3", "./home/extract_tables.py", "AKIAIKAYEL47XIFILKHQ", "ef6io24vgw1tq6uXmv3uyPZe5uftbBJYudi3i2HW", "0000051143", "0000051143-13-000007"]