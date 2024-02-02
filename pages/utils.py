import requests


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
                return data["result"][0]["text"]

            else:
                print(
                    f"Failed to upload image. Status code: {response.status_code}")
                return None
    except Exception as e:
        print(f"Error: {e}")


# Example usage:
# image_path = "carimage.jpg"
# ocr_image(image_path)


def send_sms_hook(api_token, sender_id, phone_numbers, message_body, gateway='direct-refund', append_sender='hosted'):
    """
    Send an SMS using the BulkSMSNigeria API.

    Parameters:
        - api_token (str): API token generated on the API Settings Page.
        - sender_id (str): Preferred sender ID (up to 11 characters).
        - phone_numbers (str or list): Single phone number or a list of comma-separated phone numbers.
        - message_body (str): The message body/content.
        - gateway (str): Optional, default is 'direct-refund'. Choose from available options.
        - append_sender (str): Optional, default is 'hosted'. Choose from available options.

    Returns:
        - dict: Response JSON or error message.
    """
    # Endpoint URL
    url = "https://www.bulksmsnigeria.com/api/v2/sms"

    # Header parameters
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }

    # Convert phone_numbers to a string if it's a list
    if isinstance(phone_numbers, list):
        phone_numbers = ','.join(map(str, phone_numbers))

    # Body parameters
    body_data = {
        'from': sender_id,
        'to': phone_numbers,
        'body': message_body,
        'api_token': api_token,
        'gateway': gateway,
        'append_sender': append_sender
    }

    try:
        # Making the POST request
        response = requests.post(url, json=body_data, headers=headers)

        # Checking the response
        response_data = response.json()

        if response.ok:
            print("Message sent successfully!")
            print(response_data)
            return response_data
        else:
            return {'error': f"Failed to send message. Status Code: {response.status_code}. Response: {response_data}"}

    except requests.RequestException as e:
        return {'error': f"Request Exception: {str(e)}"}



# result = send_sms(api_token, sender_id, phone_numbers, message_body)
# print(result)
