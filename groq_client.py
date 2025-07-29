from groq import Groq
import os
import base64
from PIL import Image
from io import BytesIO
import numpy as np
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

def frame_to_base64(frame):
    img = Image.fromarray(frame)
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

def analyze_frame_with_groq(frame):
    img_b64 = frame_to_base64(frame)
    content = [
        {"type": "text", "text": "Describe what is happening in this image."},
        {"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{img_b64}"}}
    ]
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[{"role": "user", "content": content}],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        stop=None
    )
    return completion.choices[0].message.content
    