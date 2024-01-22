import reflex as rx
from frontend_reflex.styles.styles import Size
from frontend_reflex.components.links_buttons import link_button
from frontend_reflex.components.title import title
import frontend_reflex.constants as const


def body() -> rx.Component:
    return rx.vstack(
        title("Social Media"),
        link_button(
            "icons/instagram.svg",
            "Instagram",
            "Follow me on instagram",
            const.TWITCH_URL,
        ),
        link_button(
            "icons/github.svg",
            "Github",
            "Follow me on github",
            const.TWITCH_URL,
        ),
        link_button(
            "icons/linkedin.svg",
            "LinkedIn",
            "Follow me on linkedIn",
            const.TWITCH_URL,
        ),
        link_button(
            "icons/twitch.svg",
            "Twitch",
            "Follow me on twitch",
            const.TWITCH_URL,
        ),
        link_button(
            "icons/x-twitter.svg",
            "X",
            "follow me on X",
            const.TWITTER_X_URL,
        ),
        link_button(
            "icons/code-solid.svg",
            "Retos de programacion",
            "Retos de programacion de Mourde Dev",
            const.CODE_CHALLENGES_URL,
        ),
        title("Contact me"),
        link_button(
            "icons/telegram.svg",
            "Telegram",
            "Text me at Telegram",
            const.TELEGRAM_URL,
        ),
        link_button(
            "icons/envelope-solid.svg",
            "Mail",
            "Send me an email at carlosmperez2901@gmail.com",
            const.EMAIL,
        ),
        margin_y=Size.BIG.value,
        width="100%",
        spacing=Size.SMALL.value,
        padding_x=Size.MEDIUM.value,
    )
