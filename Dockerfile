# Use the official Ubuntu 20.04 image
FROM ubuntu:20.04

# Set the working directory inside the container
WORKDIR /app

# Create the output directory
RUN mkdir output

# Install system dependencies
RUN apt-get update && apt-get install -y python3 python3-pip curl && \
    curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && \
    chmod +x kubectl && \
    mv kubectl /usr/local/bin/

# Install Kubeflow Pipelines SDK
RUN pip3 install kfp==1.7.0  # Use the version that corresponds to your Kubeflow version

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy the application files into the container
COPY . ./

# Expose the port that your application will run on
EXPOSE 8000

# Command to run your application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000", "--root-path", "/"]
