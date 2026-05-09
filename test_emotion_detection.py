from EmotionDetection import emotion_detector

def test_emotion_detector():

    test_cases = {
        "I am glad this happened": "joy",
        "I am really mad about this": "anger",
        "I feel disgusted just hearing about this": "disgust",
        "I am so sad about this": "sadness",
        "I am really afraid that this will happen": "fear"
    }

    for text, expected_emotion in test_cases.items():

        response = emotion_detector(text)

        dominant_emotion = response['dominant_emotion']

        if dominant_emotion == expected_emotion:
            print(f"PASS: '{text}' -> {dominant_emotion}")
        else:
            print(f"FAIL: '{text}'")
            print(f"Expected: {expected_emotion}")
            print(f"Got: {dominant_emotion}")


# Run the tests
test_emotion_detector()