import os
from google import genai

client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

business = os.environ.get("BEACON_BUSINESS", "Example Restaurant")
query = os.environ.get(
    "BEACON_QUERY",
    "How visible is this business in Google search?",
)

response = client.models.generate_content(
    model="gemini-3.6-flash",
    contents=f"""
You are Beacon by Reedstar.
Analyze this business's search visibility.

Business: {business}
Question: {query}

Return:
- observation
- evidence
- recommendation
""")

print(response.text)
