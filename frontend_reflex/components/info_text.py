import reflex as rx
from frontend_reflex.styles.colors import Color, TextColor

from frontend_reflex.styles.styles import Size


def info_text(title: str, body: str) -> rx.Component:
    return rx.box(
        rx.span(
            title,
            font_wieght="bold",
            color=Color.PRIMARY.value,
        ),
        f" {body}",
        font_size=Size.SMALL.value,
        color=TextColor.BODY.value,
    )
