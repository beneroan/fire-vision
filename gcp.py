from google.cloud import automl_v1beta1
from google.cloud.automl_v1beta1.proto import service_pb2
import sys

# 'content' is base-64-encoded image data.
def get_prediction(content, project_id, model_id):
   prediction_client = automl_v1beta1.PredictionServiceClient()

   name = 'projects/{}/locations/us-central1/models/{}'.format(project_id, model_id)
   payload = {'image': {'image_bytes': content }}
   params = {}
   request = prediction_client.predict(name, payload, params)
   return request   # waits till request is returned

if __name__ == '__main__':
   file_path = sys.argv[1]
   project_id = sys.argv[2]
   model_id = sys.argv[3]

   with open(file_path, 'rb') as ff:
      content = ff.read()

   print(get_prediction(content, project_id, model_id).payload[0].display_name)
