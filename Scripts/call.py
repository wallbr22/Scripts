import requests
from simple_salesforce import Salesforce

# Salesforce connection
sf = Salesforce(username='your_username', password='your_password', security_token='your_token')
data = sf.query("SELECT Id, Name, Phone FROM Account")

# Five9 connection
five9_url = "https://api.five9.com/rest-api/outbound-call-endpoint"  # Replace with the actual endpoint
headers = {
    "Authorization": "Bearer YOUR_FIVE9_TOKEN",
    "Content-Type": "application/json"
}

def initiate_call(phone_number):
    """Initiates a call using Five9 API and returns the response."""
    payload = {
        "phoneNumber": phone_number,
        # Add other necessary data here
    }
    response = requests.post(five9_url, headers=headers, json=payload)
    return response

# Loop through numbers until a call is picked up
call_picked_up = False
for record in data["records"]:
    if call_picked_up:
        break

    phone_number = record["Phone"]
    response = initiate_call(phone_number)

    # Check the response for call status (adjust this based on actual API response)
    if response.status_code == 200:
        call_status = response.json().get("status", "")

        if call_status == "no_answer":
            print(f"No answer from {phone_number}. Moving to next number.")
        elif call_status == "answered":
            print(f"Call was picked up by {phone_number}.")
            call_picked_up = True
        else:
            print(f"Received unknown status from {phone_number}: {call_status}. Moving to next number.")
    else:
        print(f"Error calling {phone_number}: {response.text}")

if not call_picked_up:
    print("Tried all numbers, but none answered.")
