import reflex as rx
import datetime

from frontend_reflex.styles.styles import Size
from frontend_reflex.styles.colors import Color, TextColor


def footer() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.image(src="elgato.png", height=Size.EXTRA_BIG.value),
            rx.image(src="mvp.png", height=Size.EXTRA_BIG.value),
        ),
        rx.image(src="favicon.ico"),
        rx.link(
            rx.box(
                rx.span(f"© 2014-{datetime.date.today().year}"),
                rx.span(" MoureDev by Brais Moure", color=Color.PRIMARY.value),
                rx.span(" v3."),
            ),
            href="https://mouredev.com",
            is_external=True,
        ),
        rx.text("""BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD."""),
        margin_top=Size.BIG.value,
        color=TextColor.FOOTER.value,
        padding_x=Size.MEDIUM.value,
    )
