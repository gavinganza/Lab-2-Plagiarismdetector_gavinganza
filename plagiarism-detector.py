import string
import os

# ---------------------------------------------
# 1. TEXT PROCESSING FUNCTION
# ---------------------------------------------
def process_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    for p in string.punctuation:
        text = text.replace(p, "")

    # Split into words
    words = text.split()

    # Define stop words
    stop_words = ["a", "an", "the", "is", "in", "of", "and", "to", "for", "on", "with", "at", "by"]

    # Filter out stop words
    clean_words = []
    for word in words:
        if word not in stop_words:
            clean_words.append(word)

    return clean_words


# ---------------------------------------------
# 2. WORD SEARCH FUNCTION
# ---------------------------------------------
def word_search(word, essay1_words, essay2_words):
    word = word.lower()
    count1 = essay1_words.count(word)
    count2 = essay2_words.count(word)
    return count1, count2


# ---------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------
def main():
    # Read essay files
    try:
        with open("essays/essay1.txt", "r") as f1:
            raw1 = f1.read()
        with open("essays/essay2.txt", "r") as f2:
            raw2 = f2.read()
    except FileNotFoundError:
        print("Error: essay1.txt or essay2.txt is missing in the essays/ directory.")
        return

    # ---------------------------------------------
    # Process text
    # ---------------------------------------------
    essay1_words = process_text(raw1)
    essay2_words = process_text(raw2)

    # ---------------------------------------------
    # Word Search
    # ---------------------------------------------
    search_word = input("Enter a word to search in the essays: ")
    count1, count2 = word_search(search_word, essay1_words, essay2_words)

    print("\nWORD SEARCH RESULT")
    print(f"'{search_word}' appears {count1} times in essay1.txt")
    print(f"'{search_word}' appears {count2} times in essay2.txt\n")

    # ---------------------------------------------
    # COMMON WORDS REPORT
    # ---------------------------------------------
    common_words = set(essay1_words).intersection(set(essay2_words))

    print("COMMON WORDS IN BOTH ESSAYS:")
    print(common_words)
    print()

    # ---------------------------------------------
    # JACCARD SIMILARITY (Plagiarism %)
    # ---------------------------------------------
    set_essay1 = set(essay1_words)
    set_essay2 = set(essay2_words)

    intersection = set_essay1.intersection(set_essay2)
    union = set_essay1.union(set_essay2)

    plagiarism_percentage = (len(intersection) / len(union)) * 100

    print(f"Plagiarism Percentage: {plagiarism_percentage:.2f}%")

    if plagiarism_percentage >= 50:
        print("Similarity is likely!")
    else:
        print("Similarity is low.")

    # ---------------------------------------------
    # SAVE REPORT IF USER WANTS
    # ---------------------------------------------
    save = input("\nDo you want to save the report? (y/n): ").lower()

    if save == "y":
        # Ensure "reports" directory exists
        if not os.path.exists("reports"):
            os.makedirs("reports")

        with open("reports/similarity_report.txt", "w") as report:
            report.write("COMMON WORDS FOUND:\n")
            for word in sorted(intersection):
                report.write(word + "\n")

        print("Report saved as reports/similarity_report.txt\n")

    print("Done.")


# Run program
if __name__ == "__main__":
    main()
