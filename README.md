The API service of tutorin.tech.

## Dependencies

* Python 3.8 or higher.

## Getting started

1. Create a virtual environment.

    ```bash
    $ virtualenv -ppython3 tit-api-env
    (tit-api-env) $ source ./tit-api-env/bin/activate
    (tit-api-env) $ cd tit-api
    (tit-api-env) $ pip install -r requirements.txt
    ```

2. Run PostgreSQL.

   ```bash
   (tit-api-env) $ docker run --rm --name postgres -v $(pwd)/_postgres:/var/lib/postgresql/data -e POSTGRES_PASSWORD=secret -p 5432:5432 -d postgres:13
   (tit-api-env) $ docker run --rm -it --link postgres:postgres -e PGPASSWORD=secret postgres:13 createdb -h postgres -U postgres tit-api
   ```

3. Apply the migrations.

   ```bash
   (tit-api-env) $ env SECRET=secret python3 manage.py migrate
   ```

4. Run the application.

   ```bash
   (tit-api-env) $ env SECRET=secret python3 manage.py runserver 0.0.0.0:8001
   ```
