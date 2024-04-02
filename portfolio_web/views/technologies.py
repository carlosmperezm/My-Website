import reflex as rx
from portfolio_web.components.link_button import link_button

from portfolio_web.constants import Data
from portfolio_web.styles.styles import Rx_Size, Size


def technologies() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "TECHNOLOGIES",
            as_="h4",
            size=Rx_Size.XL,
            style={"text-decoration": "underline"},
            margin_bottom=Size.XS,
        ),
        rx.chakra.responsive_grid(
            *[
                rx.box(
                    link_button(data[1], data[0], tecnology, Rx_Size.M),
                    margin=Size.XS,
                    width=Size.XXXL,
                )
                for tecnology, data in Data.TECNOLOGIES.items()
            ],
            columns=[2, 3, 4, 5, 6],
            spacing_x=Rx_Size.XXXL,
        ),
    )