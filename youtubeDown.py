import yt_dlp
import os

def download_video():
    url = input("Enter the YouTube video URL: ")

    # Set default save path to Downloads folder
    save_path = input("Enter the folder to save the video (leave blank for default Downloads folder):")
    if not save_path:
        save_path = os.path.join(os.path.expanduser("~"), "Downloads")

    print("\nChoose the file format:")
    print("1. MP4")
    print("2. MP3")
    print("3. GIF (Not Working)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        format_code = 'best'  # Best quality video
        extension = 'mp4'
    elif choice == '2':
        format_code = 'bestaudio/best'  # Best quality audio
        extension = 'mp3'
    elif choice == '3':
        format_code = 'best[ext=mp4]'  # MP4 for GIF conversion
        extension = 'gif'
    else:
        print("Invalid choice!")
        return

    # Construct the full path for the output file
    output_file = os.path.join(save_path, f"%(title)s.{extension}")

    ydl_opts = {
        'format': format_code,  # Get the best quality video
        'outtmpl': output_file,
        'postprocessors': [
            {
                'key': 'FFmpegExtractAudio',  # For MP3
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
        ] if choice == '2' else ([  # For GIF
            {
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'gif',
            }
        ] if choice == '3' else [])
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Download completed! Saved to: {save_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

download_video()
