import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput import keyboard

SPEED = 0.005 

print("Launching Chrome Browser...")
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://monkeytype.com")

print("Waiting for initial page elements to load...")
wait = WebDriverWait(driver, 10)
typing_box = wait.until(EC.presence_of_element_located((By.ID, "wordsInput")))

def wait_for_f6():
    f6_pressed = False
    def on_press(key):
        nonlocal f6_pressed
        if key == keyboard.Key.f6:
            f6_pressed = True
            return False
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

try:
    while True:
        print("\n[READY] Press F6 to start the typing test...")
        wait_for_f6()
        print("F6 pressed! Target locked and typing engine live.\n")
        
        # Refresh the typing box reference in case the test restarted
        try:
            typing_box = wait.until(EC.presence_of_element_located((By.ID, "wordsInput")))
        except:
            pass

        while True:
            try:
                active_word_element = driver.find_element(By.CSS_SELECTOR, ".word.active")
            except:
                print("Test complete or no active word found. Waiting for next F6...")
                break
                
            letters = active_word_element.find_elements(By.TAG_NAME, "letter")
            word_text = "".join([letter.text for letter in letters])
            
            if SPEED == 0:
                typing_box.send_keys(word_text + " ")
            else:
                for letter in word_text:
                    typing_box.send_keys(letter)
                    time.sleep(SPEED)
                typing_box.send_keys(" ")
                time.sleep(SPEED)
                
            time.sleep(0.02)

except Exception as error:
    print(f"An unexpected interruption occurred: {error}")
    
print("Bot execution completed!")