import reflex as rx
from portfolio_web.components.link_button import link_button
from portfolio_web.components.link import link


from portfolio_web.styles.styles import Rx_Size, Size


def info(
    title, descryption=[], links=[], technologies=[], image="", time="", certification=""
) -> rx.Component:
    return rx.flex(
        rx.box(
            *(
                (
                    rx.vstack(
                        link_button("devicon-github-plain", links[0]),
                        margin_right=Size.M,
                        margin_bottom=Size.M,
                    )
                    if links
                    else rx.box()
                ),
            ),
        ),
        rx.vstack(
            rx.heading(
                title,
                as_="h3",
                size=Rx_Size.L,
                color_scheme="sky",
            ),
            *[rx.list_item(descrypt, color_scheme="gray") for descrypt in descryption],
            rx.hstack(
                *[rx.box(class_name=tecnology) for tecnology in technologies],
                font_size=Size.M,
                margin_top=Size.XS,
            ),
        ),
        rx.spacer(),
        rx.vstack(
            rx.box(
                *(
                    (
                        rx.button(
                            link("shield-check", certification),
                            color="fff",
                            margin_y=Size.S,
                        )
                        if len(certification) > 1
                        else rx.box()
                    ),
                ),
                align="end",
                margin_left=Size.XXL,
                # margin_y=Size.S,
            ),
            rx.text(time, color_scheme="gray"),
            rx.box(
                *(
                    (
                        rx.image(
                            src=image,
                            max_width=Size.XXXL,
                            margin_left=Size.L,
                            margin_bottom=Size.S,
                        )
                        if len(image) > 1
                        else rx.box()
                    ),
                ),
            ),
            align="center",
        ),
        width="100%",
        flex_direction=["column", "row"],
        margin_top=Size.XS,
    )
