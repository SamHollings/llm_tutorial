"""Functions which are useful for working with Google Colab."""

def is_colab():
    """Returns True if the code is running in Google Colab."""
    try:
        import google.colab
        print('Running on Colab')
        return True
    except ImportError:
        return False    
    

def setup_environment():
    """Sets up the environment for Google Colab."""
    !git clone https://github.com/SamHollings/llm_tutorial.git -q
    %cd llm_tutorial 
    !pip install -r requirements.txt -q -q


def upload_env_file():
    from google.colab import files
    import os
  # Check if file already exists
    if os.path.exists('.env'):
        os.remove('.env')

    # Upload file
    uploaded = files.upload()
    file_name = list(uploaded.keys())[0]

    # Rename file
    try:
        os.rename(file_name, '.env')
        print('File uploaded and renamed successfully.')
    except:
        print('Error renaming file.')