FROM python:3.11.4

	# Set environment variables
	ENV PYTHONDONTWRITEBYTECODE 1
	ENV PYTHONUNBUFFERED 1

	# Set the working directory
 	
	WORKDIR /app

	RUN apt-get update && apt-get install -y \
		build-essential \ 
		git \
		gunicorn \
		python3-dev \
  		command-not-found \
		pgloader
	# install dependencies
 	
	RUN pip install --upgrade pip

	COPY ./requirements.txt /app
 	COPY ./manage.py /app
	RUN pip install -r requirements.txt
	


	# Copy the project code into the container
	
 	COPY . /app
  	RUN python manage.py makemigrations
 	RUN python manage.py migrate
 	RUN pgloader ./db.sqlite3 postgresql://finalp_user:vrVlqog32vqbwsJznxvPJfVWol6ALFdZ@dpg-crb7k33tq21c73cg3lng-a/finalp
	
  
 	ENTRYPOINT [ "gunicorn", "finalP.wsgi", "-b", "0.0.0.0:8000"]
