# Step 1: Base image
FROM python:3.11

# Step 2: Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


# Step 3: Create and set the working directory
WORKDIR /app

# Step 4: Install Python dependencies
# Copy the requirements.txt file and install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Step 5: Copy project files
COPY . /app/

# Step 6: Collect static files
# RUN python manage.py collectstatic --noinput

# Step 7: Expose the desired port
EXPOSE 8000

# Step 8: Run the application
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
# CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
