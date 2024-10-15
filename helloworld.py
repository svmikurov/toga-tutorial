import  toga
from toga.style import Pack

btn_style = Pack(
    padding=0,
    flex=1,
)


def button_handler(widget):
    print('hello')


def build(app):
    box = toga.Box()

    btn_1 = toga.Button('1', style=btn_style, on_press=button_handler)
    btn_1.style.flex = 1
    btn_2 = toga.Button('2', style=btn_style, on_press=button_handler)
    btn_2.style.flex = 1
    btn_3 = toga.Button('3', style=btn_style, on_press=button_handler)
    btn_3.style.flex = 2

    button = toga.Button('Hello world', on_press=button_handler)
    button.style.padding = 50
    button.style.flex = 1

    # box.add(button)
    box.add(btn_1, btn_2, btn_3)

    return box


def main():
    return toga.App(
        "First App",
        "org.beeware.toga.tutorial",
        startup=build
    )


if __name__ == '__main__':
    main().main_loop()
