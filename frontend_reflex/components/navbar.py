import reflex as rx
from frontend_reflex.styles.colors import Color

from frontend_reflex.styles.styles import Size


def navbar() -> rx.Component:
    return rx.hstack(
        rx.heading(
            rx.box(
                rx.span("Moure", color=Color.PRIMARY.value),
                rx.span("dev", color=Color.SECONDARY.value),
            ),
            size="lg",
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        z_index="999",
        width="100%",
        padding_x=Size.DEAULT.value,
        padding_y=Size.SMALL.value,
        top="0",
    )
