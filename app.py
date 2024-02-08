import talklocal
from talklocal import core
from talklocal.models import OutputFormat

import asyncio


user_input = talklocal.models.UserInput(
  source_language="en-US",
  target_language="es",
  subtitle_format= "vtt",
  region="us-east-1",
  output_format=OutputFormat.BOTH_TEXT
)

async def main():
  await core.process_request(user_input)

if __name__ == "__main__":
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main())
  loop.close()


