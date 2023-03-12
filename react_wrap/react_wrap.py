"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class State(pc.State):
    """The app state."""
    pass

class ColorPicker(pc.Component):
    library = "react-colorful"
    tag = "HexColorPicker"
    color: pc.Var[str]

    @classmethod
    def get_controlled_triggers(cls) -> dict[str, pc.Var]:
        return {"on_change": pc.EVENT_ARG}

class ColorPickerState(pc.State):
    color: str = "#db114b"

def index():
    color_picker = ColorPicker.create
    return pc.box(
        pc.vstack(
            pc.heading(ColorPickerState.color),
            color_picker(
                on_change=ColorPickerState.set_color
            ),
        ),
        background_color=ColorPickerState.color,
        padding="5em",
        border_radius="1em",
    )

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index)
app.compile()
