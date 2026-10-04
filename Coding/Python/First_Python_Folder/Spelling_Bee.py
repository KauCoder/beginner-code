import WPM_Test

# Override settings inside the main module
WPM_Test.MODE = "Hard"
WPM_Test.SCRIPTS = False
WPM_Test.SPEED = 0.1
WPM_Test.DELAY = 0

def main():
    # 1. Grab a single random word from the pool
    word = WPM_Test.random.choice(WPM_Test.WORDS)
    
    # 2. Text-to-speech audio engine speaks the word out loud
    WPM_Test.extensionslib.say_ext(word)
    
    # 3. Start the timer
    start_time = WPM_Test.extensionslib.time.time()
    
    # Fix: Clean up the syntax so it inputs text correctly based on settings
    if WPM_Test.SCRIPTS == False:
        user = input("> ")
    else:
        print("> ", end="", flush=True)
        user = WPM_Test.Script(word)
        
    # 4. Stop the timer
    end_time = WPM_Test.extensionslib.time.time()
    
    # 5. Call your calculation function (passing the required word context)
    wpm, accuracy, time_elapsed = WPM_Test.Get_WPM(user, word, start_time, end_time)
    
    # 6. Output the stats clearly
    print(f"\nStats for '{word}':")
    print(f"    WPM:      {wpm}")
    print(f"    Accuracy: {accuracy:.1f}%".replace(".0", ""))
    print(f"    Time:     {round(time_elapsed, 2)}s")

if __name__ == "__main__":
    while True:
        main()
        again = input("\nNext word? (Y/n) ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break