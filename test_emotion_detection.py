import unittest
from EmotionDetection.emotion_detection import emotion_detector

class EmotionDetectionTest(unittest.TestCase):
    def test_emotion_detector(self):
        emotion1 = emotion_detector("I am glad this happened")
        emotion2 = emotion_detector("I am really mad about this")
        emotion3 = emotion_detector("I feel disgusted just hearing about this")
        emotion4 = emotion_detector("I am so sad about this")
        emotion5 = emotion_detector("I am really afraid that this will happen")
        print("running test 1")
        self.assertEqual(emotion1["dominant_emotion"],  "joy")
        print("running test 2")
        self.assertEqual(emotion2["dominant_emotion"], "anger")
        print("running test 3")
        self.assertEqual(emotion3["dominant_emotion"], "disgust")
        print("running test 4")
        self.assertEqual(emotion4["dominant_emotion"], "sadness")
        print("running test 5")
        self.assertEqual(emotion5["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()