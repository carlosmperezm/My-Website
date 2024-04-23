import reflex as rx

from portfolio_web.components.info import info
from portfolio_web.constants import Data


def study():
    return rx.center(
        rx.vstack(
            rx.heading(
                "EDUCATION ",
                as_="h3",
                style={"text-decoration": "underline"},
            ),
            *[
                (
                    info(
                        study["title"],
                        study["descryption"],
                        tecnologies=study["tecnologies"],
                        image=study["image"],
                        time=study["time"],
                    )
                )
                for study in Data.STUDIES
            ],
        ),
        width="100%",
    )
