import reflex as rx

from portfolio_web.constants import Data

from portfolio_web.components.info import info
from portfolio_web.styles.styles import Size


def project() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "PROJECTS",
            style={"text-decoration": "underline"},
            margin_bottom=Size.XS,
        ),
        *[
            (
                info(
                    project["title"],
                    project["descryption"],
                    project["links"],
                    project["tecnologies"],
                    # image=project["image"],
                    # time=project["time"],
                )
            )
            for project in Data.PROJECTS
        ],
        width="100%",
    )
