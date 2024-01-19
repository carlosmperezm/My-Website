import reflex as rx
from frontend_reflex.styles.styles import title_style


def title(text: str) -> rx.Component:
    return rx.heading(
        text,
        style=title_style,
        size="md",
    )
