import base64
import json
from google.cloud import bigquery

PROJECT_ID = 'vertex-ai-mlops-369716'
bq = bigquery.Client(project = PROJECT_ID)
TABLE_ID = f'{PROJECT_ID}.pixel_tracking.pixel-tracking-data'

# Triggered from a message on pubsub topic, which is sent by cloud function that collect events
def pixel_tracking_data(event, context):
    
    # decode the data input, convert to python dictionary
    function_input = json.loads(
        base64.b64decode(event['data']).decode('utf-8')
    )
    
    errors = bq.insert_rows_json(TABLE_ID, [function_input])
    if errors:
        raise RuntimeError(f'BigQuery streaming insert errors: {errors}')
