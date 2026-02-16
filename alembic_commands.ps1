pip install alembic
# ADD OUR SQL URL TO THE alembic.ini FILE driver://user:pass@localhost/dbname with no qoutes
# add to the env.py in alembic the line: target_metadata = models.Base.metadata and import the models.py file and 
alembic init alembic_env_name
alembic revision -m "Added phone numbers to users" #--autogenerate # Creates a file in the alembic_env_name/versions folder with a unique identifier and the message you provided. with Revision ID

# TO run the migration and update the database schema
alembic upgrade revision_ID

# To downgrade the database schema to a previous version
alembic downgrade -1 # or revision ID, only do it when necessary, as it can lead to data loss if not done carefully. Always backup your database before downgrading.