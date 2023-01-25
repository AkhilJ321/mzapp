from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials

  
# open method used to open different extension image file

ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/"
prediction_key = "c8816cd72fba48caa5f6c1af3ed4220d"
prediction_key2 = "c8816cd72fba48caa5f6c1af3ed4220d"
prediction_resource_id = "/subscriptions/10b0f1ee-d5b8-44c5-8d92-05d91ad208c2/resourceGroups/imageclassification/providers/Microsoft.CognitiveServices/accounts/fruit"
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
prediction_credentials2 = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key2})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
predictor2 = CustomVisionPredictionClient(ENDPOINT, prediction_credentials2)
projectid = '497fdfd0-2128-494d-8e22-2984d21be39d'
projectid2='8270c9da-fd3c-47cb-a2a0-6199102c2f8f'
name = 'Iteration1'
name2 = 'iteration1'
def pred(img):

 results = predictor.classify_image(
        projectid,name, img)
 for prediction in results.predictions:

        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))
        return prediction
def detect(img):
       results = predictor2.detect_image(
        projectid2,name2, img)
       return results.predictions
