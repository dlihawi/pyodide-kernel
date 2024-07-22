from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        # Test case for joy emotion
        result_1 = emotion_detector('I love working with Python')
        self.assertEqual(result_1['emotion'], 'joy')
        
        # Test case for anger emotion
        result_1 = emotion_detector('I am really mad about this')
        self.assertEqual(result_1['emotion'], 'anger')
        
        # Test case for disgust emotion
        result_1 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_1['emotion'], 'disgust')

        # Test case for sadness emotion
        result_1 = emotion_detector('I am so sad about this')
        self.assertEqual(result_1['emotion'], 'sadness  ')

        # Test case for fear emotion
        result_1 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_1['emotion'], 'fear')


    unittest.main()
