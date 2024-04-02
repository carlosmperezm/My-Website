import reflex as rx

from portfolio_web.constants import Data
from portfolio_web.styles.styles import Size


def about_me() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "ABOUT ME",
            as_="h2",
            style={"text-decoration": "underline"},
            margin_bottom=Size.XS,
        ),
        rx.text(Data.ABOUT_ME),
    )
