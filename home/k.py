from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials

  
# open method used to open different extension image file

ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com/"
prediction_key = "c8816cd72fba48caa5f6c1af3ed4220d"
prediction_resource_id = "/subscriptions/10b0f1ee-d5b8-44c5-8d92-05d91ad208c2/resourceGroups/imageclassification/providers/Microsoft.CognitiveServices/accounts/fruit"
prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
projectid = '497fdfd0-2128-494d-8e22-2984d21be39d'
name = 'Iteration1'
def pred(img):

 results = predictor.classify_image(
        projectid,name, img)
 for prediction in results.predictions:

        print("\t" + prediction.tag_name +
              ": {0:.2f}%".format(prediction.probability * 100))
        return prediction