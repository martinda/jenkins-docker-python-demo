# Obtained from https://github.com/docker-library/repo-info/blob/master/repos/python/tag-details.md#python360
# We nail the image digest for reproducibility
FROM python@sha256:d7728edb9e52abc58552cec26d871f474394f3ffdefbe2929da93bfa42d92b1f

# The python version in the container is owned by the OS of the container
# We need to isolate our project from the OS requirements by installing the virtualenv
RUN pip install virtualenv==15.1.0

# Where the project files will be installed and tested inside the container
WORKDIR /tmp/app

# Copy the project files to the WORKDIR
COPY requirements.txt requirements.txt

# Setup the venv and install pyinstaller
RUN virtualenv /tmp/venv && \
    . /tmp/venv/bin/activate && \
    pip install -r requirements.txt
