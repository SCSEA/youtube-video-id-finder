import re

def extract_youtube_video_id(url):
    """
    Function to extract the YouTube video ID from a given URL.
    """
    # Regular expression pattern to match YouTube video IDs
    pattern = r'(?:youtube\.com\/(?:[^\/\n\s]+\/\S+\/|(?:v|e(?:mbed)?)\/|\S*?[?&]v=)|youtu\.be\/)([a-zA-Z0-9_-]{11})'
    
    # Find all matches of the pattern in the URL
    matches = re.findall(pattern, url)
    
    if matches:
        # Return the first match (YouTube video ID)
        return matches[0]
    else:
        return None

# Take the first YouTube URL as input from the user
youtube_url1 = input("Enter the YouTube URL to find the ID: ")

# Take the second YouTube URL as input from the user (if available)
youtube_url2 = input("Enter the second YouTube URL to find the ID (Press Enter to skip): ")

# Extract video ID for the first YouTube URL
video_id1 = extract_youtube_video_id(youtube_url1)
print(f"Video ID for '{youtube_url1}': {video_id1}")

# Extract video ID for the second YouTube URL (if provided)
if youtube_url2.strip():  # Check if the string is not empty after removing leading/trailing whitespace
    video_id2 = extract_youtube_video_id(youtube_url2)
    print(f"Video ID for '{youtube_url2}': {video_id2}")
else:
    print("Second YouTube URL not provided. Skipping...")
