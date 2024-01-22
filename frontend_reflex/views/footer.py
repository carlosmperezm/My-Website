import reflex as rx
import datetime

from frontend_reflex.styles.styles import Size
from frontend_reflex.styles.colors import Color, TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.link(
            rx.box(
                rx.span(f"© 2023-{datetime.date.today().year}"),
                rx.span(" Carlos Perez", color=Color.PRIMARY.value),
            ),
            href="https://carlosperezm.com",
            is_external=True,
        ),
        rx.text(
            rx.span("Email: "),
            rx.span(
                "carlosmperez2901@gmail.com", as_="b", color=TextColor.HEADER.value
            ),
        ),
        rx.text("""BUILDING SOFTWARE WITH ♥ FROM LOS ANGELES TO THE WORLD."""),
        margin_top=Size.BIG.value,
        color=TextColor.FOOTER.value,
        padding_x=Size.MEDIUM.value,
    )
