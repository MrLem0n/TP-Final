from nicegui import ui

from arbolPrueba import raiz,simular_for
with ui.row().classes('w-full items-center'):
    # result = ui.label().classes('mr-auto')
    # with ui.button(icon='menu'):
    #     with ui.menu() as menu:
    #         ui.menu_item('Menu item 1', lambda: result.set_text('Selected item 1'))
    #         ui.menu_item('Menu item 2', lambda: result.set_text('Selected item 2'))
    #         ui.menu_item('Menu item 3',lambda: result.set_text('Selected item 3'))
    #         ui.separator()
    #         ui.menu_item('Close', menu.close)

    simular_for(raiz)

ui.run()