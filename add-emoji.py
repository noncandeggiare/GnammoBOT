import json
import nltk
from nltk.tokenize import sent_tokenize

def load_emoji_map(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        emoji_map = json.load(file)
    return emoji_map

def add_emojis_to_sentences(message, emoji_map):
    nltk.download('punkt')
    
    sentences = sent_tokenize(message)
    
    formatted_message = ''
    for sentence in sentences:
        emoji = None
        for keywords, emote in emoji_map.items():
            for keyword in keywords:
                if keyword in sentence.lower():
                    emoji = emote
                    break
            if emoji:
                break
        
        if emoji:
            formatted_message += f'{emoji} {sentence}\n'
        else:
            formatted_message += f'{sentence}\n'
    
    return formatted_message

# Load emoji map from an external file
emoji_map_file = 'emoji_map.json'
emoji_map = load_emoji_map(emoji_map_file)

# Read message from output.md file
with open('output.md', 'r', encoding='utf-8') as file:
    message = file.read()

# Process message with emojis
formatted_message = add_emojis_to_sentences(message, emoji_map)
print(formatted_message)
