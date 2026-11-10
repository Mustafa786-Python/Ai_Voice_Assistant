# Voice Temperature Assistant

This project is a voice assistant built with LiveKit Agents and Gemini Live. It lets you check and change simulated room temperatures by speaking.

## What it can do

You can ask questions such as:

- “What is the temperature in the bedroom?”
- “Set the kitchen to 26.”
- “What is the temperature in the office?”
- “Set the bathroom to 18 degrees.”

The assistant supports these rooms: living room, bedroom, kitchen, bathroom, and office.

## How it works

1. You speak to the assistant.
2. Your audio travels through a LiveKit room.
3. Gemini Live handles speech input and speech output with the `Puck` voice. The project has no separate speech-to-text or text-to-speech components.
4. Gemini Live asks the assistant to call `get_temperature` or `set_temperature`.
5. The tool reads or changes the in-memory temperature.
6. The assistant speaks the result.

```text
Your voice
    |
    v
LiveKit room
    |
    v
Gemini Live <----> Assistant tool
                         |
                         v
                 In-memory temperatures
```

The assistant starts with these temperatures:

| Room | Temperature |
|---|---:|
| Living room | 22 °C |
| Bedroom | 20 °C |
| Kitchen | 24 °C |
| Bathroom | 23 °C |
| Office | 21 °C |

## Project files

| File | Purpose |
|---|---|
| [`api.py`](api.py) | Defines the supported rooms and the assistant tools for reading and changing temperatures. |
| [`main.py`](main.py) | Loads environment variables, creates the LiveKit agent server, and starts a Gemini Live session. |

## Requirements

- Python 3.10 or newer
- A LiveKit Cloud project
- A Gemini API key

## Install on Ubuntu

Create the virtual environment outside the project folder:

```bash
python3 -m venv ~/venvs/ai-voice-assistant
source ~/venvs/ai-voice-assistant/bin/activate
```

This repository does not contain a `requirements.txt` file. Install the packages directly:

```bash
pip install "livekit-agents[google]~=1.8" python-dotenv
```

[TODO: generate requirements.txt with pip freeze]

## Configure

Create a `.env` file in the project folder:

```dotenv
LIVEKIT_URL=https://your-livekit-project-url
LIVEKIT_API_KEY=your-livekit-api-key
LIVEKIT_API_SECRET=your-livekit-api-secret
GOOGLE_API_KEY=your-google-api-key
```

Never commit `.env` or its credentials. The repository's `.gitignore` lists `.env`.

The variable names above come from the LiveKit and Google documentation, not from the Python code.

## Run

For a local console session using your microphone and speakers:

```bash
python3 main.py console
```

To connect to the LiveKit Agents Playground:

```bash
python3 main.py dev
```

The LiveKit CLI marks console mode as deprecated. Check the current LiveKit documentation for the current command.

The agent uses automatic dispatch to new rooms. The code does not set an agent name.

## Try it

1. Start the console or Playground session and wait for the assistant to greet you.
2. Ask, “What is the temperature in the bedroom?” It should report 20 degrees Celsius.
3. Say, “Set the kitchen to 26.” Then ask for the kitchen temperature again. You can also try “Set the kitchen to 40.” The assistant should say that it can only set a temperature between 10 and 35 degrees Celsius.

## Troubleshooting

- `ModuleNotFoundError: No module named 'dotenv'`: activate the virtual environment before running the project.
- No sound or a flat microphone meter: check the audio devices with `python3 main.py console --list-devices`.
- The agent does not join: check all four values in `.env`.
- Gemini quota errors: check the quota for the Google API key.
- Gemini model name errors: check the current Gemini Live model and LiveKit Google plugin documentation.

## Limits

The temperatures are simulated. They do not control real devices. The values are stored in memory and reset when the program restarts.

The project has not been verified on a live connection: [TODO: state what you tested].

## Planned work

- Connect a dashboard to LiveKit.
- Save temperatures to a file or database.
- Control a real device, such as an ESP32.

## License

MIT — see [`LICENSE`](LICENSE).
