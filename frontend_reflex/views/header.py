import reflex as rx
from frontend_reflex.components.info_text import info_text
from frontend_reflex.styles.styles import Size
from frontend_reflex.styles.colors import TextColor, Color
from frontend_reflex.components.link_icon import link_icon
import frontend_reflex.constants as const

descryption_text: str = """Soy ingeniero de software y actualmente trabajo como freelance
            full-stack developer iOS y Android.  Además, creo contenido formativo sobre
            programación en redes.  Aquí podrás encontrar todos mis enlaces de interés
            ¡Bienvenid@!"""


def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                name="Brais Moure",
                src="avatar.jpg",
                size="xl",
                padding="2px",
                border="4px",
                border_color=Color.PRIMARY.value,
            ),
            rx.vstack(
                rx.heading("Brais Moure", size="md", color=TextColor.HEADER.value),
                rx.text(
                    "@mouredev", margin_top="0 !important", color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon("icons/github.svg", const.GITHUB_URL, "github"),
                    link_icon("icons/x-twitter.svg", const.TWITTER_X_URL, "twitter/x"),
                    link_icon("icons/instagram.svg", const.INSTAGRAM_URL, "instagram"),
                    link_icon("icons/tiktok.svg", const.TIKTOK_URL, "tiktok"),
                    link_icon("icons/spotify.svg", const.SPOTIFY_URL, "spotify"),
                    link_icon("icons/linkedin.svg", const.LINKEDIN_URL, "linkedin"),
                    spacing=Size.DEAULT.value,
                ),
                align_items="start",
            ),
            spacing=Size.MEDIUM.value,
        ),
        rx.flex(
            info_text("14+", "annos de experiencia"),
            rx.spacer(),
            info_text("100+", "aplicaciones creadas"),
            rx.spacer(),
            info_text("1M+", "seguidores"),
            width="100%",
            color=TextColor.HEADER.value,
        ),
        rx.text(descryption_text, color=TextColor.BODY.value),
        margin_y=Size.BIG.value,
        align_items="start",
        spacing=Size.BIG.value,
        padding_x=Size.MEDIUM.value,
    )
