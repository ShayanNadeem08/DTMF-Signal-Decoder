# DTMF Signal Decoder

This repository contains a Python project that generates Dual-Tone Multi-Frequency (DTMF) signals for different digits and provides a decoder to identify the corresponding digit from an audio file. DTMF signals are used in telecommunication systems to represent digits or keys pressed on a telephone keypad.

## How DTMF Signals Work

DTMF signals are composed of two sine waves with different frequencies. In the case of telephone keypads, a combination of two frequencies is used to represent each digit. For example, the digit 5 is represented by a sum of two sine waves with frequencies of 770Hz and 1336Hz.

![image](https://github.com/ShayanNadeem08/DTMF-Signal-Decoder/assets/135377655/23b36dfc-5fc7-426e-b095-6f965cb9d600)
![image](https://github.com/ShayanNadeem08/DTMF-Signal-Decoder/assets/135377655/5d47a3a9-1f2f-4aeb-9620-d8e486d07962)


## Project Structure

The project consists of the following components:

- `dtmf_trail.py`: This Python script generates DTMF signals for digits 1 and 2. It utilizes sine waves of specific frequencies and adds them together to create the DTMF signals.

- `dtmf_main.py`: This Python script provides a decoder to identify the corresponding digit from an audio file containing DTMF signals. It employs signal processing techniques to analyze the input audio and match it with the appropriate digit.

- `dtmf_signal/`: This directory contains audio samples of DTMF signals for a unique digit. We have to decode this sample to figure out from which digit it shows the highest resemblance.

## Getting Started

To use this project, follow these steps:

1. Clone this repository to your local machine using `git clone https://github.com/your-username/dtmf-signal-decoder.git`.

2. Install the required dependencies by running `pip install -r requirements.txt`.

3. Collect audio samples of DTMF signals for each digit by recording or obtaining them from external sources. Save these samples in the `audio_samples/` directory.

4. Run the `dtmf_decoder.py` script, providing the path to the audio file as an argument. The decoder will process the audio and determine the corresponding digit.

5. Make sure the `dtmf_signal.wav`(the audio file you are working on i.e decoding) file must be in your cd.

Feel free to explore and modify the project according to your needs.
