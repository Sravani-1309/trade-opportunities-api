from google import genai
import os
print("API KEY:", os.getenv("GEMINI_API_KEY"))
# create client using environment variable
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
def analyze_data(data: str, sector: str):
    try:
        prompt = f"""
        Analyze the {sector} sector in India.

        Provide:
        - Key insights
        - Trade opportunities
        - Risks

        Data:
        {data}
        """

        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        print("AI ERROR:", e)

        return f"""
- The {sector} sector is growing in India
- Investment opportunities increasing
- Risks include competition and regulation
"""