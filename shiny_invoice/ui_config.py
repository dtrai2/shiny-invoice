"""
This module contains the ui and server for the configuration view. It simply displays the
configuration inside the shiny invoice application
"""

import io

from ruamel.yaml import YAML
from shiny import module, ui, render

yaml = YAML(typ="rt", pure=True)


@module.ui
def config_ui():
    """Defines the shiny ui for the configuration"""
    return ui.div(ui.card(ui.card_header("Configuration"), ui.output_code("config_output")))


@module.server
def config_server(input, output, session, config):
    """Contains the shiny server for the configuration view"""

    @render.text
    def config_output():
        """Dump the configuration into a string and return it"""
        buffer = io.BytesIO()
        yaml.dump(config, buffer)
        return buffer.getvalue().decode("utf8")
