import reflex as rx
from frontend_reflex.styles.styles import Size
from frontend_reflex.components.links_buttons import link_button
from frontend_reflex.components.title import title
import frontend_reflex.constants as const


def body() -> rx.Component:
    return rx.vstack(
        title("Comunidad"),
        link_button(
            "icons/twitch.svg",
            "Twitch",
            "Directos de lunes a viernes",
            const.TWITCH_URL,
        ),
        link_button(
            "icons/youtube.svg",
            "Youtube",
            "Videos de programacion semanales",
            const.YOUTUBE_URL,
        ),
        link_button(
            "icons/discord.svg",
            "Discord",
            "Server de la comunidad",
            const.DISCORD_URL,
        ),
        link_button(
            "icons/code-solid.svg",
            "Retos de programacion",
            "Ejercicios semanales para practicar logica de programacion",
            const.CODE_CHALLENGES_URL,
        ),
        link_button(
            "icons/youtube.svg",
            "Youtube (canal segundario)",
            "Videos de programacion semanales",
            const.YOUTUBE_SECONDARY_URL,
        ),
        # Secon section
        title("Recursos y mas"),
        link_button(
            "icons/git-alt.svg",
            "Git y Guthub desde cero",
            "Aqui puedes comprar mi libro en formato fisico y eBook",
            const.BOOK_URL,
        ),
        link_button(
            "icons/book-solid.svg",
            "Libros recomandados",
            "mi listado de libros sobre programacion, ciencia y tecnologia",
            const.BOOKS_URL,
        ),
        link_button(
            "icons/laptop-solid.svg",
            "Mi setup",
            "Listado de todos los elementos que uso en mi trabajo",
            const.SETUP_URL,
        ),
        link_button(
            "icons/logo.png",
            "MoureDev",
            "Mi sitio web",
            const.MOUREDEV_URL,
        ),
        link_button(
            "icons/mug-hot-solid.svg",
            "Invitame un cafe",
            "Quieres ayudarme a que siga creando contenido?",
            const.COFFEE_URL,
        ),
        # Contact
        title("Contacto"),
        link_button(
            "icons/check-solid.svg",
            "MyPublicInbox",
            "respuesta rapida y con preferencia",
            const.MYPUBLICINBOX_URL,
        ),
        link_button(
            "icons/envelope-solid.svg",
            "Email",
            "braismoure@mouredev.com",
            const.EMAIL,
        ),
        margin_y=Size.BIG.value,
        width="100%",
        spacing=Size.SMALL.value,
        padding_x=Size.MEDIUM.value,
    )
