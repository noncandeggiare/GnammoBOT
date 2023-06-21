import json

# Load the emoji map from emoji_map.json using utf-8 encoding
with open('emoji_map.json', encoding='utf-8') as f:
    emoji_map = json.load(f)

# Open output.md and read its content
with open('output.md', encoding='utf-8') as f:
    content = f.readlines()

# Find the index where "Oggi si mangia:" appears
index = next((i for i, line in enumerate(content) if 'Oggi si mangia:' in line), None)

if index is not None:
    # Create a list to store the updated menu items
    updated_menu = []

    # Iterate over the menu items starting from the index
    for item in content[index+1:]:
        item = item.strip()
        if item:
            # Split the item into words and find the first word present in the emoji map
            words = item.split()
            for word in words:
                if word.lower() in emoji_map:
                    emoji = emoji_map[word.lower()]
                    updated_menu.append(f'{emoji} {item.replace("- ", "", 1)}\n')
                    break  # Stop searching for words once an emoji is found

    # Update the content with the updated menu items
    content = content[:index+1] + updated_menu

    # Write the updated content back to output.md with utf-8 encoding
    with open('output.md', 'w', encoding='utf-8') as f:
        f.writelines(content)