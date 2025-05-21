import airflow
from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator
from datetime import datetime,timedelta

#define variable
PROJECT_ID='mynewproject-454707'
DATASET1="raw_ds"
DATASET2="insight_ds" 
TABLE_1="emp"
TABLE_2="dept"
TABLE_3="emp_dept"

INSERT_ROWS_QUERY="""
CREATE OR REPLACE TABLE {PROJECT_ID}.{DATASET2}.{TABLE_3}
AS 
SELECT 
e.employee_id,concat(e.first_name," ",e.last_name) as fullName,e.email,e.hire_date,e.salary,
d.department_name,d.manager_id
from {PROJECT_ID}.{DATASET1}.{TABLE_1} e left join 
{PROJECT_ID}.{DATASET1}.{TABLE_2} d on 
e.department_id =d.department_id

"""



args={
    "owner" : "Mansi Shinde",
    "start_date" : datetime(2025,4,9),
    "retries" : 1,
    "retry_delay" : timedelta(minutes=5)
}


#define dag
with DAG(
    'myfirstDag',
    schedule_interval='3 22 * * *',
    default_args=args,
    description= "gcs to bigquery"

) as DAG:



#define task 

    t1 = GCSToBigQueryOperator(
        task_id="taskone",
        bucket="mybicket-use",
        source_objects=["employee.csv"],
        destination_project_dataset_table=f"{DATASET1}.{TABLE_1}",
        schema_fields=[
            {"name": "employee_id", "type": "STRING", "mode": "NULLABLE"},
            {"name": "first_name", "type": "STRING", "mode": "NULLABLE"},
            {"name": "last_name", "type": "STRING", "mode": "NULLABLE"},
            {"name": "email", "type": "STRING", "mode": "NULLABLE"},
            {"name": "department_id", "type": "STRING", "mode": "NULLABLE"},
            {"name": "hire_date", "type": "STRING", "mode": "NULLABLE"},
            {"name": "salary", "type": "STRING", "mode": "NULLABLE"},
                  
        ],
        write_disposition="WRITE_TRUNCATE",
    )



    t2 = GCSToBigQueryOperator(
        task_id="tasktwo",
        bucket="mybicket-use",
        source_objects=["department.csv"],
        destination_project_dataset_table=f"{DATASET1}.{TABLE_2}",
        schema_fields=[
            {"name": "department_id", "type": "STRING", "mode": "NULLABLE"},
            {"name": "department_name", "type": "STRING", "mode": "NULLABLE"},
            {"name": "manager_id", "type": "STRING", "mode": "NULLABLE"},
        ],
        write_disposition="WRITE_TRUNCATE",
    )

#Insert into table 

    t3 = BigQueryInsertJobOperator(
        task_id="insertempdept",
        configuration={
            "query": {
                "query": INSERT_ROWS_QUERY,
                "useLegacySql": False,
                "priority": "BATCH",
            }
        },
    )

 #dependancy 
(t1,t2)>>t3