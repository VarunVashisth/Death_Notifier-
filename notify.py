import asyncio
from desktop_notifier import DesktopNotifier
from pydub import AudioSegment
from pydub.playback import play
import random


notify = DesktopNotifier(app_name="Death-Notifier")

with open("/home/varizz/Desktop/Death_Notifier-/qoutes/data.txt", "r") as f:
    quotes = [line.strip() for line in f if line.strip()]


async def main():



    while True:
        # Pick a random quote
        quote = random.choice(quotes)

        # Show notification
        await notify.send(
                        title="DEATH",
                        message=quote,

                    )
        

        path = "/home/varizz/Desktop/Death_Notifier-/audio/brainrot.mp3"
        sound = AudioSegment.from_file(path)
        clip = sound[:3000]
        play(clip)

        # Random wait time between notifications (30 min to 5 hrs)
        wait_seconds = random.randint(30*60, 5*60*60)
        print(f"Next Notification in : {wait_seconds}" )

        await asyncio.sleep(wait_seconds)

     


asyncio.run(main())
