import reflex as rx
from portfolio_web.components.link_button import link_button

from portfolio_web.constants import Data
from portfolio_web.styles.styles import Rx_Size, Size


def contact_buttons() -> rx.Component:
    return rx.flex(
        rx.link(
            rx.button(rx.icon("mail"), Data.MAIL),
            href=f"mailto:{Data.MAIL}",
            is_external=True,
            margin_bottom=Size.S,
        ),
        rx.flex(
            rx.link(rx.icon(tag="linkedin"), href=Data.LINKEDIN, is_external=True),
            rx.link(rx.icon(tag="github"), href=Data.GITHUB, is_external=True),
            rx.link(rx.icon(tag="file-text"), href=Data.CV, is_external=True),
            spacing=Rx_Size.M,
            margin_left="0.8em",
        ),
        flex_direction=["column"],
        spacing=Rx_Size.S,
    )
