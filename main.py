from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentServer, AgentSession
from livekit.plugins import google

from api import Assistant

# Load the LiveKit and Google credentials from the .env file.
load_dotenv()

# Create the server that receives LiveKit room sessions.
server = AgentServer()


# Start one Gemini Live session whenever LiveKit dispatches this agent.
@server.rtc_session()
async def entrypoint(ctx: agents.JobContext):
    # Gemini Live handles speech recognition and speech output.
    session = AgentSession(
        llm=google.realtime.RealtimeModel(voice="Puck"),
    )

    # Start the session with the temperature-control assistant.
    await session.start(room=ctx.room, agent=Assistant())

    # Ask Gemini Live to greet the user.
    await session.generate_reply(
        instructions="Greet the user and ask how you can help."
    )


if __name__ == "__main__":
    # Run the server with automatic dispatch to new rooms.
    agents.cli.run_app(server)


#Connect the dashboard with livekit