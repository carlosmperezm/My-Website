"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from portfolio_web.styles.styles import Size, STYLESHEETS, BASE_STYLE, Rx_Size
from portfolio_web.views.about_me import about_me
from portfolio_web.views.certification import certification
from portfolio_web.views.footer import footer
from portfolio_web.views.header import header
from portfolio_web.views.project import project
from portfolio_web.views.studies import study
from portfolio_web.views.technologies import technologies
from portfolio_web.views.experience import experience


def index() -> rx.Component:
    return rx.center(
        rx.vstack(
            # rx.theme_panel(),
            header(),
            about_me(),
            rx.divider(),
            technologies(),
            project(),
            certification(),
            experience(),
            study(),
            rx.divider(),
            footer(),
            padding=Size.M,
            spacing=Rx_Size.XL,
        ),
        padding=Size.M,
    )


# Create app instance and add index page.
app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(appearance="dark", accent_color="blue", radius="full"),
)
app.add_page(
    index,
    title="",
    description="",
    meta=[],
)
