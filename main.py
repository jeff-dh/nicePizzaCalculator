from nicegui import ui, app
from nicegui.observables import ObservableDict


# default recipe per kilo flour
default_base_recipe = dict(
    Mehl = 1000,
    Wasser = 580,
    Salz = 30,
    Hefe = 5,
    Soße = 520,
    Käse = 600,
    Gemüse = 600,
    )

default_piece_weight = 210

# names of ingredients
ingredients = list(default_base_recipe.keys())


def calcRecipe(pieces,
               piece_weight=default_piece_weight,
               base_recipe=None):
    base_recipe = base_recipe or dict(default_base_recipe)

    required_dough = pieces * piece_weight if pieces else 0

    # Summe aller Zutaten pro Kilo Mehl
    dough_per_kilo_flour = (1000 + base_recipe["Wasser"]
                                 + base_recipe["Salz"]
                                 + base_recipe["Hefe"])

    factor  = required_dough / dough_per_kilo_flour

    return {k: f"{v * factor:.0f}g" for k, v in base_recipe.items()}


def config_dialog(cfg):
    """the config dialog to adjust the recipe"""

    def ingredient_edit(name):
        ui.number(label=f"{name}/kg Mehl", on_change=show_recipe.refresh)\
            .bind_value(cfg["base_recipe"], name)

    with ui.dialog() as dialog, ui.card():
        with ui.column().classes("flex justify-center items-center"):
            ui.markdown("###Grundrezept")

            with ui.card():
                ui.markdown("#####Teig")

                ui.number(label="Teigling-Größe", on_change=show_recipe.refresh)\
                    .bind_value(cfg, "piece_weight")

                [ingredient_edit(k) for k in ingredients[1:4]]

            with ui.card():
                ui.markdown("#####Belag")

                [ingredient_edit(k) for k in ingredients[4:]]

            with ui.row().classes("w-full"):
                def reset_config():
                    cfg["piece_weight"] = default_piece_weight
                    cfg["base_recipe"].update(ObservableDict(default_base_recipe))

                ui.button("Zurücksetzen", on_click=reset_config)
                ui.space()
                ui.button("Schließen", on_click=dialog.close)

    return dialog


@ui.refreshable
def show_recipe(cfg):
    """calculation and output of the resulting recipe"""

    recipe = calcRecipe(cfg["pieces"],
                        cfg["piece_weight"],
                        cfg["base_recipe"])

    with ui.grid(columns=2).classes("w-full"):

        def ingredients_card(title, start, end):
            with ui.card():
                ui.markdown(f"######{title}:")
                with ui.row():
                    with ui.column(align_items="end"):
                        for i in range(start, end):
                            ui.label(f"{ingredients[i]}").classes("font-bold")
                    with ui.column(align_items="start"):
                        for i in range(start, end):
                            ui.label(f"{recipe[ingredients[i]]}")

        ingredients_card("Teig", 0, 4)
        ingredients_card("Belag", 4, len(ingredients))


@ui.page("/", title="PizzaCalculator")
def index():
    # init config
    app.storage.user["base_recipe"] = app.storage.user.get("base_recipe", ObservableDict(default_base_recipe))
    app.storage.user["pieces"] = app.storage.user.get("pieces", 8)
    app.storage.user["piece_weight"] = app.storage.user.get("piece_weight", default_piece_weight)
    cfg = app.storage.user

    # init config dialog
    dialog = config_dialog(cfg)

    #main card
    with ui.card().classes("mx-auto max-w-md w-full").style("background-color: lightgray;"):

        # header
        ui.markdown("###**PizzaCalculator**")\
                .classes("w-full text-center")\
                .style("background-color: #EEEEEE;")

        # body
        with ui.card().classes("w-full"):

            ui.button("Grundrezept", icon="settings", on_click=dialog.open).classes("w-full")

            # Anzahl der Teiglinge
            ui.number(label="Teiglinge", on_change=show_recipe.refresh)\
                .bind_value(app.storage.user, "pieces")\
                .classes("w-full")

            show_recipe(cfg)


def is_android():
    import platform
    return 'android' in platform.uname().release

if not is_android():
    ui.run(storage_secret='blablub')
else:
    ui.run(host='localhost', reload=False, storage_secret='blablub', show=False)
