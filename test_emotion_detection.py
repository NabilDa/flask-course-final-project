from EmotionDetection.emotion_detection import emotion_detector
import unittest

"""
This is a unit test for the function emotion_detector
"""
class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        dominant_emotion_1 = emotion_detector("I am glad this happened")["dominant_emotion"]
        self.assertEqual(dominant_emotion_1, "joy")
        
        dominant_emotion_2 = emotion_detector("I am really mad about this")["dominant_emotion"]
        self.assertEqual(dominant_emotion_2, "anger")

        dominant_emotion_3 = emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"]
        self.assertEqual(dominant_emotion_3, "disgust")

        dominant_emotion_4 = emotion_detector("I am so sad about this")["dominant_emotion"]
        self.assertEqual(dominant_emotion_4, "sadness")

        dominant_emotion_5 = emotion_detector("I am really afraid that this will happen")["dominant_emotion"]
        self.assertEqual(dominant_emotion_5, "fear")

unittest.main()
