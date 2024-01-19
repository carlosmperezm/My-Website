import reflex as rx
from enum import Enum
from frontend_reflex.styles.styles import Size, button_body_style, button_title_style


class links(Enum):
    TWITTER = "https//x.com"
    FACEBOOK = "https//facebook.com"


def link_button(img_src: str, title: str, descryption: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.image(
                    src=img_src,
                    width=Size.MEDIUM.value,
                    height=Size.MEDIUM.value,
                ),
                rx.vstack(
                    rx.text(title, style=button_title_style),
                    rx.text(descryption, style=button_body_style),
                    align_items="start",
                ),
            ),
        ),
        href=url,
        is_external=True,
        width="100%",
        padding=Size.SMALL.value,
    )
