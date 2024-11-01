import os

content = f"""FROM {os.environ['BASE_IMAGE']}

# Install pip and upgrade it
RUN pip install --upgrade pip

# Set the working directory
WORKDIR /workspace

# Copy the current directory contents into the container
COPY . /workspace

# Install the package in editable mode with dev dependencies
RUN pip install -e .[dev]
"""
file_name = "Dockerfile"
