import reflex as rx


def link(icon, url, text="", color="white") -> rx.Component:
    return rx.link(
        rx.icon(icon),
        text,
        href=url,
        is_external=True,
        color=color,
    )
