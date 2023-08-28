#Speed_Typing_test

import time

def typing_test(text):
    print("Type the following text:")
    print(text)
    input("Press Enter when you're ready...")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()

    correct_chars = sum(a == b for a, b in zip(text, user_input))
    accuracy = (correct_chars / len(text)) * 100
    elapsed_time = end_time - start_time
    words_per_minute = (len(user_input) / 5) / (elapsed_time / 60)

    print("\nResults:")
    print("Time taken: {:.2f} seconds".format(elapsed_time))
    print("Accuracy: {:.2f}%".format(accuracy))
    print("Words per minute: {:.2f}".format(words_per_minute))

if __name__ == "__main__":
    test_text = "This is a typing speed test. Try to type this accurately and quickly."
    typing_test(test_text)