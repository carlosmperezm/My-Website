import reflex as rx

from portfolio_web.components.info import info
from portfolio_web.constants import Data


def certification():
    return rx.vstack(
        rx.heading(
            "CERTIFICATIONS ",
            as_="h3",
            style={"text-decoration": "underline"},
        ),
        *[
            (
                info(
                    certification["title"],
                    certification["descryption"],
                    # tecnologies=certification["tecnologies"],
                    image=certification["image"],
                    certification=certification["certification"],
                )
            )
            for certification in Data.CERTIFICATIONS
        ],
        width="100%",
    )
