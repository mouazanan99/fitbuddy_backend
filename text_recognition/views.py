from rest_framework import generics
from rest_framework.response import Response
from .serializers import ResponseSerializer
import spacy


nlp = spacy.load('ner_model')

# Define Questions
heart_rate_reponse ='Your heart rate is:'
oxygen_level_reponse ='Your oxygen level is:'

# Get the correct response for the given question from the NER model
def getResponse(question):
  response = nlp(question)
  if response.ents:
    for ent in response.ents:
      if "oxygen" in ent.text:
       return oxygen_level_reponse
      elif "heart" in ent.text:
       return heart_rate_reponse
      else :
       print("sorry")


# Question Response API
class QuestionResponseAPI(generics.GenericAPIView):
    serializer_class = ResponseSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        questionModel = serializer.save()
        answer = getResponse(questionModel.question)
        return Response({
        "status": 0,
        "message": "Success",
        "response": answer
        })

 