
[database]
database_host = localhost
database_name = airflow_reddit
database_port = 5432
database_username = postgres
database_password = postrgres

[file_paths]
input_path = /opt/airflow/data/input
output_path = /opt/airflow/data/output

[api_keys]
reddit_secret_key = [SECRET KEY HERE]
reddit_client_id = [CLIENT ID HERE]

[aws]
aws_access_key_id = [aws access key id]
aws_secret_access_key= [aws secret key]
aws_session_token= [aws session token]
aws_region = [aws region]
aws_bucket_name = [s3 bucket name]

[etl_settings]
batch_size = 100
error_handling = abort
log_level = info
