import reflex as rx
from portfolio_web.constants import Data

from portfolio_web.components.info import info


def experience() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading(
                "EXPERIENCE",
                style={"text-decoration": "underline"},
            ),
            *[
                info(
                    title=experience["rol"],
                    descryption=experience["descryption"],
                    tecnologies=experience["tecnologies"],
                    time=experience["time"],
                    image="UCF Logo.png",
                )
                for experience in Data.EXPERIENCE
            ],
        ),
        width="100%",
    )
