from difflib import SequenceMatcher

with open ('hi.txt') as f1, open ('hi2.txt') as f2:

    data_file1 = f1.read()
    data_file2 = f2.read()

    matches = SequenceMatcher(None, data_file1, data_file2).ratio()

    print( matches*100, " content is plagiarised ")
