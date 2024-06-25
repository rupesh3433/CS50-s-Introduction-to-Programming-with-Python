import re

def main():
    print(parse(input("HTML: ")))

def parse(s):
    url_pattern = r"<iframe[^>]*(?:https?:)?//(?:www\.)?youtube\.com/embed/([\w-]+)[^>]*>"
    match = re.search(url_pattern, s)
    if match:
        video_id = match.group(1)
        shorter_format = f"https://youtu.be/{video_id}"
        return shorter_format
    return None

if __name__ == "__main__":
    main()
