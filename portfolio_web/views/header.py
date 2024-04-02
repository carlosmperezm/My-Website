import reflex as rx
from portfolio_web.components.contact_buttons import contact_buttons

from portfolio_web.constants import Data
from portfolio_web.styles.styles import Rx_Size, Size


def header() -> rx.Component:
    return rx.flex(
        rx.avatar(src="/profile.jpg", size=Rx_Size.XXL, margin_top=Size.M),
        rx.vstack(
            rx.heading(
                Data.NAME,
                as_="h1",
                size=Rx_Size.XXL,
                margin_left="-0.1em",
            ),
            rx.heading(
                Data.ROLE,
                as_="h3",
                size=Rx_Size.L,
                color_scheme="sky",
            ),
            rx.text(
                rx.icon(
                    tag="map-pin",
                    margin_x="0.8em",
                ),
                "Whittier, CA",
                display="inherit",
            ),
            contact_buttons(),
            spacing=Rx_Size.M,
        ),
        spacing=Rx_Size.XL,
        flex_direction=["column", "column", "row"],
    )
