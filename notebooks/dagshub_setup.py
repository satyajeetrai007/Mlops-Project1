
import mlflow
import dagshub


mlflow.set_tracking_uri('https://dagshub.com/satyajeetrai007/Mlops-Project1.mlflow')
dagshub.init(repo_owner='satyajeetrai007', repo_name='Mlops-Project1', mlflow=True)



with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

