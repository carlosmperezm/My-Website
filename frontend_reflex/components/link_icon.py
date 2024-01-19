import reflex as rx

from frontend_reflex.styles.styles import Size


def link_icon(img_src: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(src=img_src, height=Size.MEDIUM.value, alt=alt),
        href=url,
        is_external=True,
    )
