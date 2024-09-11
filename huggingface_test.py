# Transaltion Techniques Models

##################################################################################################################################

 # 1. Helsinki-NLP (OPUS-MT):(DEFAULT MODELS FOR TRANSALTION)

    # A.Helsinki-NLP/opus-mt-en-de: English to German
    # B.Helsinki-NLP/opus-mt-fr-en: French to English
    # C.Helsinki-NLP/opus-mt-es-en: Spanish to English
    # D.Helsinki-NLP/opus-mt-en-it: English to Italian



# from transformers import pipeline

# # Load the translation pipeline with a specific model you want to use.
# translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de") #English to German used

# # Translate text
# text = "Hello, how are you?"
# translation = translator(text)
# print(translation[0]['translation_text'])  




from transformers import pipeline

# Load the translation pipeline with a specific model you want to use.
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-fr-en") #French to English used

# Translate text
text = "Bonjour, comment ça va aujourd'hui?"
translation = translator(text)
print(translation[0]['translation_text'])  




# from transformers import pipeline

# # Load the translation pipeline with a specific model you want to use.
# translator = pipeline("translation", model="Helsinki-NLP/opus-mt-es-en") #Spanish to english used

# # Translate text
# text = "Hola, ¿cómo estás hoy?"
# translation = translator(text)
# print(translation[0]['translation_text'])  






# from transformers import pipeline

# # Load the translation pipeline with a specific model you want to use.
# translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-it") #English to Italian used

# # Translate text
# text = "I would like to order a coffee, please."
# translation = translator(text)
# print(translation[0]['translation_text'])  


# ###########################################################################################################################################


# # 2. google-t5/t5-small languages supporting : English(en), French(fr), Romanian(ro), German(de), multilingual

# from transformers import pipeline

# # Load the translation pipeline for a specific language pair
# translator = pipeline("translation", model="google-t5/t5-small")

# # Translate text
# text = "Hello, how are you?"
# translation = translator(text, src_lang="en", tgt_lang="fr") #English to French
# print("English to French:", translation[0]['translation_text'])

