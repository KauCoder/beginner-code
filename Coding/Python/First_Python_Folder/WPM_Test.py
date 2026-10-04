import random
import extensionslib
import WPM_Test_Hard

# Difficulty mode
MODE = "Hard"

# Scripts settings
SCRIPTS = True
SPEED = 0.01
DELAY = 0

if MODE == "Easy":
    WORDS = [
        "person", "the", "be", "to", "of", "and", "a", "in", "that", "have", "i", 
        "it", "for", "not", "on", "with", "he", "as", "you", "do", "at", 
        "this", "but", "his", "by", "from", "they", "we", "say", "her", "she", 
        "or", "an", "will", "my", "one", "all", "would", "there", "their", "what", 
        "so", "up", "out", "if", "about", "who", "get", "which", "go", "me", 
        "when", "make", "can", "like", "time", "no", "just", "him", "know", "take", 
        "people", "into", "year", "your", "good", "some", "could", "them", "see", "other", 
        "than", "then", "now", "look", "only", "come", "its", "over", "think", "also", 
        "back", "after", "use", "two", "how", "our", "work", "first", "well", "even",
        "chargoggagoggmanchauggagoggchaubunagungamaugg"
    ]
elif MODE == "Hard":
    WORDS = WPM_Test_Hard.WORDS
    
def Script(words):
    extensionslib.script_type(words, speed=SPEED, delay=DELAY)
    return words

def Get_WPM(user_input, test_text, start_time, end_time):
    # Fix 1: Correct math direction for elapsed time
    time_elapsed = end_time - start_time
    if time_elapsed <= 0:
        time_elapsed = 0.001 # Prevent zero division error
        
    total_chars = len(user_input)
    
    # Fix 2: Calculate standard WPM based on character length
    wpm = round((total_chars / 5) / (time_elapsed / 60))
    
    # Process word accuracy metrics side-by-side
    test_words = test_text.split()
    user_words = user_input.split()
    correct_words = sum(1 for u, p in zip(user_words, test_words) if u == p)
    total_words = len(test_words)
    
    accuracy = (correct_words / total_words) * 100
    
    return wpm, accuracy, time_elapsed
    
def main(words_amount=10):
    user_input = ""
    test_construction = random.choices(WORDS, k=words_amount)
    test = " ".join(test_construction)

    print(f"\n{test}\n")

    print("Test is starting in:", end="\n\n")
    extensionslib.time.sleep(1)
    print("3", flush=True, end="")
    extensionslib.time.sleep(1)
    print("\r2", flush=True, end="")
    extensionslib.time.sleep(1)
    print("\r1", flush=True, end="")
    extensionslib.time.sleep(1)
    print("\rGo!!!", flush=True, end="\n\n")
    extensionslib.time.sleep(0.25)

    start_time = extensionslib.time.time()
    if SCRIPTS == True:
        print("Type Here: ", end="", flush=True)
        user_input = Script(test)
    else:
        user_input = input("Type Here: ")
    end_time = extensionslib.time.time()

    if len(user_input) == 0:
        print("\nTest cancelled (nothing was typed).")
        return

    # Fix 3: Call your Get_WPM function to compute data points cleanly
    wpm, accuracy, time_elapsed = Get_WPM(user_input, test, start_time, end_time)

    if wpm >= 400:
        print("\n\nYou are cheating, test invalid! :)")
    else:
        print("\n\nRESULTS:")
        print(f"    WPM:    {wpm}")
        print(f"    ACC:    {accuracy:.1f}%".replace(".0", ""))
        print(f"    TIME:   {round(time_elapsed, 2)}s")

if __name__ == "__main__":
    while True:
        main()
        again = input("\nRetry? (Y/n) ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break