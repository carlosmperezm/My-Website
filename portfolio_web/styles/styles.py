import reflex as rx


class Size:
    XXXL = "12em"
    XXL = "6em"
    XL = "4em"
    L = "3em"
    M = "2em"
    S = "1em"
    XS = "0.5em"


class Rx_Size:
    XXXL = "9"
    XXL = "8"
    XL = "6"
    L = "4"
    M = "3"
    S = "2"
    XS = "1"


STYLESHEETS = ["https://cdn.jsdelivr.net/gh/devicons/devicon@latest/devicon.min.css"]

BASE_STYLE = {
    rx.button: {"--cursor-button": "pointer"},
    rx.heading: {
        # "color": "rgba(181,246,237)",
        # ':'0'-shadow": "0 0 2px rgba(158, 208, 234, 1)",
    },
}
