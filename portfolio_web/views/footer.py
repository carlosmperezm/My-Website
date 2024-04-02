import reflex as rx
from portfolio_web.components.contact_buttons import contact_buttons

from portfolio_web.styles.styles import Rx_Size


def footer() -> rx.Component:
    return rx.vstack(
        rx.heading("Let's talk: ", as_="h3", size=Rx_Size.L), contact_buttons()
    )
