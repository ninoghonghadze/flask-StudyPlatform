FROM python:3.12

# Set working directory
WORKDIR /app

# Copy offline packages and requirements
COPY requirements.txt ./
COPY packages/ ./packages/

# Install dependencies using offline packages
RUN pip install --no-index --find-links=packages -r requirements.txt

# Copy the rest of the project
COPY . .

# Set Flask to run on all interfaces (for Docker)
CMD ["flask", "run", "--host=0.0.0.0"]
