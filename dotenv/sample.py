from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
user=os.environ.get("USER")
pswd=os.environ.get("PASSWORD")
api_key=os.environ.get("API_KEY")

print(f"user: {user}")
print(f"pswd: {pswd}")
print(f"api_key: {api_key}")