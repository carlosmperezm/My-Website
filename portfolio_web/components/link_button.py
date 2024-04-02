import reflex as rx

from portfolio_web.styles.styles import Rx_Size, Size


def link_button(icon, url, text="", btn_size=Rx_Size.L) -> rx.Component:
    return rx.link(
        rx.button(
            rx.box(class_name=icon, font_size=Size.M),
            text,
            size=btn_size,
        ),
        href=url,
        is_external=True,
    )
