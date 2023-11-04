"""functions for working with google colab"""

def upload_dot_env_file():
    """Uploads .env file to google colab."""
    import os

    from google.colab import files

    # Check if file already exists
    if os.path.exists(".env"):
        os.remove(".env")

    # Upload file
    uploaded = files.upload()
    file_name = list(uploaded.keys())[0]

    # Rename file
    try:
        os.rename(file_name, ".env")
        print("File uploaded and renamed successfully.")
    except:
        print("Error renaming file.")
