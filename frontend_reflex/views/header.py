import reflex as rx
from frontend_reflex.components.info_text import info_text
from frontend_reflex.styles.styles import Size
from frontend_reflex.styles.colors import TextColor, Color
from frontend_reflex.components.link_icon import link_icon
import frontend_reflex.constants as const

descryption_text: str = """I am a junior software engineer who is constantly
 learning and improving himself"""


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Carlos Perez",
                src="avatar.jpg",
                size="xl",
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value,
            ),
            rx.vstack(
                rx.heading("Carlos Perez", size="md", color=TextColor.HEADER.value),
                rx.text(
                    "@char_types", margin_top="0 !important", color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon("icons/github.svg", const.GITHUB_URL, "github"),
                    link_icon("icons/x-twitter.svg", const.TWITTER_X_URL, "twitter/x"),
                    link_icon("icons/instagram.svg", const.INSTAGRAM_URL, "instagram"),
                    link_icon("icons/linkedin.svg", const.LINKEDIN_URL, "linkedin"),
                    spacing=Size.DEAULT.value,
                ),
                align_items="start",
            ),
            spacing=Size.MEDIUM.value,
        ),
        rx.flex(
            info_text("2+", "years of experience"),
            rx.spacer(),
            info_text("3+", "apps created"),
            width="100%",
            color=TextColor.HEADER.value,
        ),
        rx.text(descryption_text, color=TextColor.BODY.value),
        margin_y=Size.BIG.value,
        align_items="start",
        spacing=Size.BIG.value,
        padding_x=Size.MEDIUM.value,
    )
