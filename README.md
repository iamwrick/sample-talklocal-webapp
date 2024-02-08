# TalkLocal Subtitle Generator

## Overview

This repository contains a sample Python project demonstrating the integration of TalkLocal for real-time transcription and translation of speech into subtitles. The project includes a hierarchical directory structure and sample code to facilitate easy setup and usage.

## Project Structure

The hierarchical structure of the sample Python project is as follows:


- **sample-application/**: Root directory of the project.
- **output/**: Directory to store original transcripts, translated outputs, or both in textual (.txt) files.
- **subtitle/**: Directory containing subtitle files (.vtt or .srt) based on user input.
- **static/**: Directory housing a static HTML file (`subtitle_viewer.html`) containing JavaScript (JS) for refreshing subtitles at certain intervals.
- **app.py**: Python file for the application logic, used to initiate the transcription and translation process.
- **server.py**: Python script serving as the main entry point of the sample application, utilizing Flask to render subtitles in an HTML page.

## Getting Started

To begin using the TalkLocal subtitle generator, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have Python installed on your system.
3. Navigate to the project directory in your terminal.
4. Install any required dependencies by running `pip install -r requirements.txt`.
5. Execute the following command to start the library:
   

If you prefer using an integrated development environment (IDE) such as PyCharm, you can create distinct configurations to run both `app.py` and `server.py` concurrently through the tool, enabling you to see the real-time generation of subtitles.

## User Input Parameters

The `UserInput` object in `app.py` configures source language, target language, subtitle format, and additional settings. Below are the parameters defined in the `UserInput` object:


If you prefer using an integrated development environment (IDE) such as PyCharm, you can create distinct configurations to run both `app.py` and `server.py` concurrently through the tool, enabling you to see the real-time generation of subtitles.

## User Input Parameters

The `UserInput` object in `app.py` configures source language, target language, subtitle format, and additional settings. Below are the parameters defined in the `UserInput` object:

```bash
user_input = talklocal.models.UserInput(
 source_language="en-US",
 target_language="es",
 subtitle_format="vtt",
 region="us-east-1",
 output_format=OutputFormat.TRANSLATED_TEXT
)

```

- **source_language**:Specifies the source language for transcription (e.g., English with code en-US).

- **target_language**: Defines the target language for translation (e.g., Spanish with code es).

- **subtitle_format**: Specifies the output subtitle format (vtt for WebVTT or srt for SubRip Subtitle).

- **region**: Optional parameter specifying the AWS region where the service will be executed (default: "us-east-1").

- **output_format**: Optional parameter defining the desired output format (TRANSLATED_TEXT, ORIGINAL_TRANSCRIPT, or BOTH).

## Additional Information

For a list of supported languages or language codes, refer to the Amazon Translate documentation.
To learn more about WebVTT and SubRip Subtitle formats, visit the respective documentation.

## Contributors
Feel free to contribute to this project by submitting pull requests or reporting issues.

## License
This project is licensed under the MIT License.





