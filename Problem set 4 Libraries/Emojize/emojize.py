# To use this module, at first we need to "pip install emoji"
import emoji

input_for_emoji = input("Input: ")
texual_part = input_for_emoji[:input_for_emoji.find(":")]
aliases_part = input_for_emoji[input_for_emoji.find(":"):]
print(f"Output: {texual_part}{emoji.emojize(aliases_part, language='alias')}")
