import enum
import logging

from livekit.agents import Agent, function_tool

logger = logging.getLogger("temperature-control")
logger.setLevel(logging.INFO)


class Zone(enum.Enum):
    LIVING_ROOM = "living_room"
    BEDROOM = "bedroom"
    KITCHEN = "kitchen"
    BATHROOM = "bathroom"
    OFFICE = "office"




class Assistant(Agent):
    # Set the assistant's instructions and the starting temperature for each room.
    def __init__(self) -> None:
        super().__init__(
            instructions=(
                "You are a voice assistant. Your interface with users is voice. "
                "Use short and clear answers. Do not use symbols that are hard to say "
                "out loud. You can check and change the temperature in rooms of the house."
            )
        )
        self._temperature = {
            Zone.LIVING_ROOM: 22,
            Zone.BEDROOM: 20,
            Zone.KITCHEN: 24,
            Zone.BATHROOM: 23,
            Zone.OFFICE: 21,
        }

    # Let the language model ask for the temperature in a room.
    @function_tool
    async def get_temperature(self, zone: Zone) -> str:
        """Get the current temperature in a specific room.

        Args:
            zone: The room whose current temperature should be checked.
        """
        logger.info("Getting temperature for zone: %s", zone)
        room = zone.value.replace("_", " ")
        return f"The temperature in the {room} is {self._temperature[zone]} degrees Celsius."

    # Let the language model change the temperature within the safe range.
    @function_tool
    async def set_temperature(self, zone: Zone, temp: int) -> str:
        """Set the temperature in a specific room.

        Args:
            zone: The room whose temperature should be changed.
            temp: The target temperature in degrees Celsius, from 10 to 35.
        """
        if not 10 <= temp <= 35:
            return "I can only set a temperature between 10 and 35 degrees Celsius."

        self._temperature[zone] = temp
        logger.info("Setting temperature for %s to %s degrees Celsius", zone, temp)
        room = zone.value.replace("_", " ")
        return f"The temperature in the {room} has been set to {temp} degrees Celsius."
