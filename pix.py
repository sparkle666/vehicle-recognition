import requests


def upload_image(file_path):
    # endpoint_url = "https://vehicleobs.onrender.com/api/v1/upload/"
    endpoint_url = "http://localhost:8000/api/v1/upload/"

    try:
        with open(file_path, 'rb') as file:
            files = {'image': file}
            print(f"All Files: {files}")
            response = requests.post(endpoint_url, files=files)

            if response.ok:
                print("Image uploaded successfully!")
                # print(response.json())
            else:
                print(
                    f"Failed to upload image. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")


def ocr_image(file_path):
    # endpoint_url = "https://vehicleobs.onrender.com/api/v1/upload/"
    endpoint_url = "https://jaided.ai/api/ocr"

    headers = {"username": 'SparkleSix',
               'apikey': 'IeBaoUbWiLJa3e0rbsDNjaTMGE0lJAsI'}
    # files = {'file': open('your_file_path','rb')}
    # result = requests.post(url, headers=headers, files=files).json()

    try:
        with open(file_path, 'rb') as file:
            files = {'file': file}
            print(f"All Files: {files}")
            response = requests.post(
                endpoint_url, headers=headers, files=files)

            if response.ok:
                print("Image uploaded successfully!")
                data = response.json()
                
                print(data)
                print(data["result"][0]["text"])
            else:
                print(
                    f"Failed to upload image. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")


# Example usage:
image_path = "carimage.jpg"
ocr_image(image_path)
