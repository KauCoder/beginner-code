import WPM_Test

# Override settings inside the main module
WPM_Test.MODE = "Hard"
WPM_Test.SCRIPTS = True
WPM_Test.SPEED = 0.01
WPM_Test.DELAY = 0

def main():
    word = WPM_Test.random.choice(WPM_Test.WORDS)
    WPM_Test.extensionslib.say_ext(word)
    start_time = WPM_Test.extensionslib.time.time()
    if WPM_Test.SCRIPTS == False:
        user = input("> ")
    else:
        print("> ", end="", flush=True)
        user = WPM_Test.Script(word)
    end_time = WPM_Test.extensionslib.time.time()
    wpm, accuracy, time_elapsed = WPM_Test.Get_WPM(user, word, start_time, end_time)
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