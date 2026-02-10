import asyncio
import edge_tts # type: ignore
import os

async def speak(text):
    communicate = edge_tts.Communicate(
        text,
        voice="en-IN-NeerjaNeural"
    )

    await communicate.save("voice.mp3")
    os.system("mpg123 voice.mp3")

while True:
    user = input("Write something: ")

    if user.lower() == "bye":
        break

    asyncio.run(speak(user))
