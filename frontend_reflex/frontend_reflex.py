"""Welcome to Reflex! This file outlines the steps to create a basic app."""
import reflex as rx

from frontend_reflex.styles.styles import BASE_STYLES, Size, STYLESHEETS

from frontend_reflex.views.header import header
from frontend_reflex.views.footer import footer
from frontend_reflex.views.body import body
from frontend_reflex.components.navbar import navbar


# class State(rx.State):
#     pass


def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                body(),
                max_width=Size.MAX_WIDTH.value,
            ),
        ),
        footer(),
    )


app = rx.App(
    style=BASE_STYLES,
    stylesheets=STYLESHEETS,
)

title = "MoureDev | Te enseño programación y desarrollo de software"
description = "Hola, mi nombre es Brais Moure. Soy ingeniero de software, desarrollador freelance full-stack y divulgador."
preview = "https://moure.dev/preview.jpg"

app.add_page(
    index,
    title=title,
    description=description,
    image="avatar.jpg",
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": preview},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@mouredev"},
    ],
)
