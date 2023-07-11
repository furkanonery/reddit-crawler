# reddit-crawler
Brandefense 2023 Internship Camp

# endpoints
admin/ <br />
users/ <br />
api-auth/login/ <br />
api-auth/ logout/ <br />
postsSoup/

## Installation

1. Clone the project files to your computer:

    ```
    git clone https://github.com/furkanonery/reddit-crawler.git
    ```

2. Navigate to the `core` directory:

    ```
    cd  reddit-crawler/core
    ```

3. Install the required dependencies:

    ```
    pip3 install -r requirements.txt
    ```

4. Perform Django migrations to create the database:

    ```
    python3 manage.py migrate
    ```

## Usage

### Starting Celery Worker and Beat

1. Navigate to the `core` directory:

    ```
    cd reddit-crawler/core
    ```

2. To start the Celery Worker, run the following command:

    ```
    celery -A crawler_soup worker --loglevel=info
    ```

3. To start the Celery Beat, run the following command:

    ```
    celery -A crawler_soup beat --loglevel=info
    ```

### Running the Server

1. Navigate to the `core` directory:

    ```
    cd reddit-crawler/core
    ```

2. To run the server, execute the following command:

    ```
    python3 manage.py runserver
    ```

3. Open your browser and visit `http://localhost:8000` to start using the Crawler Soup application.


### Add admin user
python3 manage.py createsuperuser
