"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
from pynecone.event import EVENT_ARG
from pynecone.var import Var

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"

class ColorPicker(pc.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: Var[str]

    @classmethod
    def get_controlled_triggers(cls) -> dict[str, Var]:
        return {
                    "on_change": EVENT_ARG,
                }

class ColorPickerState(pc.State):
    color: str = "#db114b"

def index():
    return pc.box(
        pc.vstack(
            pc.heading(ColorPickerState.color),
            ColorPicker.create(
                on_change=ColorPickerState.set_color
            ),
        ),
        background_color=ColorPickerState.color,
        padding="5em",
        border_radius="1em",
    )
# Add state and page to the app.
app = pc.App(state=ColorPickerState)
app.add_page(index)
app.compile()
