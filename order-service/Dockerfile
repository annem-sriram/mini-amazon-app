# Step 1: Choose a lightweight base image with Python pre-installed
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file first
COPY requirements.txt .

# Step 4: Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the application script
COPY app.py .

# Step 6: Inform Docker that the container listens on port 5002
EXPOSE 5002

# Step 7: Run the Flask application
CMD ["python", "app.py"]
