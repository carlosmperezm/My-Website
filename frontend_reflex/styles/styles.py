import reflex as rx
from frontend_reflex.styles.colors import Color, TextColor
from frontend_reflex.styles.fonts import Font, FontWeight
from enum import Enum

STYLESHEETS = [
    "https://fonts.googleapis.com/css2?family=Poppins:wght@300;500&display=swap",
    "https://fonts.googleapis.com/css2?family=Comfortaa:wght@500&display=swap",
]


class Size(Enum):
    SMALL = "0.7em"
    DEAULT = "1em"
    MEDIUM = "1.5em"
    BIG = "2em"
    EXTRA_BIG = "4em"
    MAX_WIDTH = "500px"


BASE_STYLES = {
    "font_family": Font.DEFAULT.value,
    "font_weight": FontWeight.LIGHT.value,
    "background_color": Color.BACKGROUND.value + "!important",
    rx.Button: {
        "width": "100%",
        "height": "100%",
        "color": TextColor.HEADER.value,
        "display": "block",
        "padding": Size.SMALL.value,
        "border_radius": Size.SMALL.value,
        "background_color": Color.CONTENT.value,
        "_hover": {"background_color": Color.SECONDARY.value},
    },
    rx.Link: {"text_decoration": "none", "_hover": {}},
}

title_style = dict(
    width="100%", padding_top=Size.SMALL.value, color=TextColor.HEADER.value
)
navbar_title_style = dict(
    font_family=Font.LOGO.value,
    font_weight=FontWeight.MEDIUM.value,
    font_size=Size.MEDIUM.value,
)
button_title_style = dict(
    font_family=Font.TITLE.value,
    font_size=Size.DEAULT.value,
    color=TextColor.HEADER.value,
)
button_body_style = dict(
    font_weight=FontWeight.LIGHT.value,
    font_size=Size.SMALL.value,
    color=TextColor.BODY.value,
)
