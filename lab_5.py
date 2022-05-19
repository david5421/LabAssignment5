"""
The program is trying to translate a sentence captured as user input.
We first read in the text file textese.txt.
then from the text file, we create a list of strings from each lines in the text file.
Then, we create a dictionary from the list.
Once the text file has been read into memory, we close the file.

We then define a function for translating which envovles splitting the user input (sentence) into an
array of strings (" enjoy the excellent band tonight")[" enjoy", "the", "excellent", "band","tonight"]

once we have the array of strings respresenting the user's input sentence, we
loop through each words, find the key mathcing and returns back the value tied to the word
in our dictionary.

After each word is translated, we then
print out the translated sentence to the user.
"""
