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

TITLE = "Carlos Perez | Software engineer. Know about me "
DESCRIPTION = "Hi i am Carlos and i am a junior software engineer seeking for a job"
PREVIEW = "https://carlosperezm/preview.jpg"

app.add_page(
    index,
    title=TITLE,
    description=DESCRIPTION,
    image="avatar.jpg",
    meta=[
        {"name": "og:type", "content": "website"},
        {"name": "og:title", "content": TITLE},
        {"name": "og:description", "content": DESCRIPTION},
        {"name": "og:image", "content": PREVIEW},
        {"name": "twitter:card", "content": "summary_large_image"},
        {"name": "twitter:site", "content": "@chartypes"},
    ],
)
