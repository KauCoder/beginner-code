import time
import random

WORDS = [
    "taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronokupokaiwhenuakitanatahu",
    "llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch",
    "chargoggagoggmanchauggagoggchaubunagungamaugg",
    "supercalifragilisticexpialidocious",
    "pneumonoultramicroscopicsilicovolcanoconiosis",
    "hexakosioihexekontahexaphobia",
    "hippopotomonstrosesquippedaliophobia",
    "bourgeoisification",
    "antidisestablishmentarianism",
    "pseudopseudohypoparathyroidism",
    "hematospectrophotometrically",
    "gegenstandstheorie",
    "canaliculodacryocystorhinostomy",
    "floccinaucinihilipilification",
    "psychoneuroendocrinological",
    "orotatephosphoribosyltransferase",
    "ribulosebisphosphatetriosephosphatelyase",
    "ribulosebisphosphatecarboxylaseoxygenase",
    "dextrodeorsumversion",
    "sclerectoiridectomy",
    "scaphotrapeziotrapezoidosteoarthritis",
    "uridinediphosphateglycosyltransferase",
    "funkenzwangsvorstellung",
    "percutaneousendoscopicgastrostomy",
    "thymicstromallymphoppoietin",
    "zoanthroprosopometamorphopsia",
    "xanthogranulomatouspyelonephritis",
    "nonanonacontanonactanonaliagon",
    "ventriculocisternostomy",
    "thyroparathyroidectomy",
    "inositolphosphorylceramide",
    "ferriprotoporphyrin",
    "pyrrolizidinealkaloidosis",
    "erythrocytapheresis",
    "corynebacteriumpseudotuberculosis",
    "corticopontocerebellar",
    "gastrocnemiosemimembranous",
    "dichlorodiphenyltrichloroethane",
    "pseudorhombicuboctahedron",
    "laryngotracheobronchitis",
    "encephalocraniocutaneouslipomatosis",
    "subcompartmentalization",
    "bromochlorodifluoromethane",

]


def main(words_amount=10):
    test_construction = random.choices(WORDS, k=words_amount)

    test = " ".join(test_construction)

    print(f"\n{test}\n")

    print("Test is starting in:", end="\n\n")
    time.sleep(1)
    print("3", flush=True, end="")
    time.sleep(1)
    print("\r2", flush=True, end="")
    time.sleep(1)
    print("\r1", flush=True, end="")
    time.sleep(1)
    print("\rGo!!!", flush=True, end="\n\n")
    time.sleep(0.25)

    start_time = time.time()
    user_input = input("Type Here: ").strip().lower()
    end_time = time.time()

    time_elapsed = end_time - start_time
    total_chars = len(user_input)

    if total_chars == 0:
        print("\nTest cancelled (nothing was typed).")

    wpm = round((total_chars / 5) / (time_elapsed / 60))

    test_words = test.split()
    user_words = user_input.split()
    
    # Safely compare individual words side-by-side
    correct_words = sum(1 for u, p in zip(user_words, test_words) if u == p)
    total_words = len(test_words)
    
    # Calculate final accuracy percentage
    accuracy = (correct_words / total_words) * 100


    print("\nRESULTS:")
    print(f"    WPM:      {wpm:.1f}".replace(".0", ""))
    print(f"    ACC:      {accuracy:.1f}%".replace(".0", ""))
    print(f"    TIME:   {round(time_elapsed, 2)}s")

if __name__ == "__main__":
    while True:
        main()
        again = input("\nRetry? (Y/n)").strip().lower()
        if again != "y":
            print("Goodbye!")
            break