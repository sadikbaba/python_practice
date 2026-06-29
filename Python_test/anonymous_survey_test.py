import unittest
from anonymose_survey import AnonymousSurvey

class test_AnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""

    def test_store_single_response(self):
         question = "what is your language"
         new_survey = AnonymousSurvey(question)
         new_survey.store_response("Hausa")
         self.assertIn("Hausa", new_survey.responses)

    def test_store_more_one_response(self):
         question = "what is your language"
         new_survey = AnonymousSurvey(question)
         responses = ['English', 'Hausa', 'Arabic']
         for response in responses:
          new_survey.store_response(response)
         for response in responses:
             self.assertIn(response, new_survey.responses)

unittest.main()