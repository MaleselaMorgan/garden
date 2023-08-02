#Import spacey function.
import spacy 

# Load the model abd assign it to a variable.
nlp = spacy.load('en_core_web_sm')


# Create a list of garden path sentences.
gardenpathSentences = [ "The old man the boat.", 
                        "The florist sent the flowers was pleased.",
                        "The cotton clothing is made of grows in Mississippi.",
                        "The sour drink from the ocean.",
                        "Have the students who failed the exam take the supplementary.",
                        "Helen is expecting tomorrow to be a bad day."
                        ]

# Iterate through the list of strings.  Tokenise each string in the list.
# Perform entity recognition.
for items in gardenpathSentences:
    doc = nlp(items)
    doc.text.split()
    print("Tokenized sentence: ")
    print([token.orth_ for token in doc])

    print("Recognised entities: ")
    print([(i, i.label_, i.label) for i in doc.ents])
    print("\n")
    

print("\n")
print("\n")

# Use spacey.explain function to unknown entities.
GPE = spacy.explain("GPE")
DATE = spacy.explain("DATE")

print(f"""GPE represents: {GPE}
DATE represents: {DATE}""")

# I looked up the teho above entities:
# GPE - The word did make sense when i looked up the entity but the accronym didnt relate.
# DATE - This was obvious. I only chose this item as my sentences only provided the two options.
