# Lab-2-Plagiarismdetector_gavinganza

## OVERVIEW
It is a Python application, which compares the similarity of two documents of text (essay1.txt and essay2.txt) using the Jaccard Similarity. It assists in the detection of possible plagiarism through text processing, common stop word removal and word frequency comparison. A helper shell script configures the necessary directory structure.

## FEATURES

### Python Application (plagiarism-detector.py)
1. **Text Processing**
- Converting the text to lowercase
- Removing punctuation
- Splitting the text into words and stored into a list
- Filtering common stop words

2. **Word Search**
- Searching for the chosen word in both essays
- counting and displaying the number of occurences in each essay

3. **Common words report**
- Determining words occuring in both essays
- Displaying the common words

4. **Plagiarism calculation**
- Implementing jacardi simmilarity "Plagiarism % = (Number of common unique words / Total unique words) * 100"
- Displays if the simillarity is above or below 50%

5. **Report saving**
- The user is given an option to either save or not save the common words in 'reports/similarity_report.txt'


## setup.sh (Shell script)
- Creates required folders: `essays/` and `reports/`
- Logs setup actions to `setup.log`

## Directory structure
Lab2-gavinganza/
│
├── plagiarism-detector.py
├── setup.sh
├── setup.log
│
├── essays/
│ ├── essay1.txt
│ └── essay2.txt
│
└── reports/

1. **Setting up the necessary directories**
### Usage
``bash
./setup.sh

2. **essays/**
   essays/essay1.txt
   essays/essay2.txt

3. **Run plagiarism detector**
   python3 plagiarism-detector.py

4. **save the results(optional)**
   
