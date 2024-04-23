import reflex as rx

from portfolio_web.styles.styles import Rx_Size, Size


def link_button(
    icon,
    url,
    text="",
    btn_size=Rx_Size.L,
) -> rx.Component:
    return rx.link(
        rx.box(
            rx.vstack(
                rx.box(class_name=icon, font_size=Size.M),
                text,
                width="100%",
                align="center",
            ),
            size=btn_size,
            href=url,
            is_external=True,
        ),
    )
