import yaml

base_url = "https://raw.githubusercontent.com/TrivadisPF/arch-diagrams/refs/heads/main/icons/building-blocks/"

import drawpyo
from os import path

file = drawpyo.File()
file.file_path = path.join("/data-transfer/")
file.file_name = "Apply_Style_From_String.drawio"
page = drawpyo.Page(file=file)

with open ("/data-transfer/config.yml", "r") as yml_file:
    config = yaml.safe_load(yml_file)


# size of the icon, both width and height
icon_size = 30

# starting position for first building block icon inside layer
bb_start_pos_x = 40
bb_start_pos_y = 45
# the amount to shift right for the new column of building blocks
bb_shift_right=60
# the amount to shift down for a new row of building blocks
bb_shift_down=80

layer_spacing = 40

for layer in config["layers"]:
    layer_name = config["layers"][layer]["name"]
    layer_top_left_x = config["layers"][layer]["top_left_x"]
    layer_top_left_y = config["layers"][layer]["top_left_y"]    
    layer_nof_cols = config["layers"][layer]["nof_cols"]
    layer_nof_rows = config["layers"][layer]["nof_rows"]
    layer_width = (layer_nof_cols * icon_size) + ( (layer_nof_cols - 1) * (bb_shift_right - icon_size) ) + 25 + 25;
    layer_heigth = (layer_nof_rows * icon_size) + ( (layer_nof_rows - 1) * (bb_shift_down - icon_size) ) + bb_start_pos_y + 40;
    #layer_heigth = config["layers"][layer]["height"]

    l_x = layer_top_left_x + (layer_width / 2)
    l_y = layer_top_left_y + (layer_heigth / 2)
    
    persistence = drawpyo.diagram.object_from_library(
        page=page,
        library="general",
        obj_name="rounded_rectangle",
        value=layer_name,
        width=layer_width,
        height=layer_heigth,
        text_format=drawpyo.diagram.TextFormat(bold=True)
        )
    persistence.apply_style_string("whiteSpace=wrap;rounded=1;dashed=0;inherit=default;html=1;verticalAlign=top;fontStyle=1;arcSize=4;fontStyle=1;")
    #persistence.apply_style_string("whiteSpace=wrap;rounded=1;strokeColor=default;dashed=0;inherit=default;spacingRight=40;spacingBottom=0;spacingLeft=3;spacingTop=1;html=1;labelBackgroundColor=none;strokeWidth=1;fontColor=default;arcSize=20;absoluteArcSize=1;horizontal=1;verticalAlign=top;align=center;fontStyle=1")
    persistence.center_position = (l_x,l_y)
    
    building_blocks = config["layers"][layer]["building_blocks"]
    
    i = 1;
    x = bb_start_pos_x;
    y = bb_start_pos_y;
    for building_block in building_blocks:
        id = list(building_block.keys())[0]
        name = building_block["name"]
        image_url = base_url + layer + "/" + id + ".png"
    
        style_str_obj = drawpyo.diagram.Object(page=page, parent=persistence, value=name, width=icon_size, height=icon_size)
        style_str_obj.apply_style_string(
            "whiteSpace=wrap;rounded=0;dashed=0;shape=image;verticalLabelPosition=bottom;labelBackgroundColor=none;verticalAlign=top;aspect=fixed;imageAspect=0;image=" + image_url + ";fontSize=10;spacing=0;"
        )
        style_str_obj.center_position = (x,y)
        x = x + bb_shift_right
        if (i % layer_nof_cols == 0):
           x = bb_start_pos_x
           y = y + bb_shift_down
        i = i + 1

# right arrow
arrow = drawpyo.diagram.object_from_library(
    page=page,
    library="flowchart",
    obj_name="transfer",
    value="",
    width=30,
    height=20,    
    text_format=drawpyo.diagram.TextFormat(bold=True)
    )
arrow.center_position=(145 + 15, 40 + 10)
arrow.apply_style_string("whiteSpace=wrap;rounded=0;fillColor=#4D4D4D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;strokeWidth=2;shape=mxgraph.arrows2.arrow;dy=0.54;dx=11.29;notch=0;fontStyle=1;fontStyle=1;")

# left arrow
arrow = drawpyo.diagram.object_from_library(
    page=page,
    library="flowchart",
    obj_name="transfer",
    value="",
    width=30,
    height=20,    
    text_format=drawpyo.diagram.TextFormat(bold=True)
    )
arrow.center_position=(145 + 15, 60 + 10)
arrow.apply_style_string("whiteSpace=wrap;rounded=0;fillColor=#4D4D4D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;strokeWidth=2;shape=mxgraph.arrows2.arrow;dy=0.54;dx=11.29;notch=0;fontStyle=1;fontStyle=1;direction=west;")

# down arrow
arrow = drawpyo.diagram.object_from_library(
    page=page,
    library="flowchart",
    obj_name="transfer",
    value="",
    width=25,
    height=35,    
    text_format=drawpyo.diagram.TextFormat(bold=True)
    )
arrow.center_position=(370 + 12.5, 120 + 17.5)
arrow.apply_style_string("whiteSpace=wrap;rounded=0;fillColor=#4D4D4D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;strokeWidth=2;shape=mxgraph.arrows2.arrow;dy=0.54;dx=11.29;notch=0;fontStyle=1;fontStyle=1;direction=south;")

# up arrow
arrow = drawpyo.diagram.object_from_library(
    page=page,
    library="flowchart",
    obj_name="transfer",
    value="",
    width=25,
    height=35,    
    text_format=drawpyo.diagram.TextFormat(bold=True)
    )
arrow.center_position=(410 + 12.5, 120 + 17.5)
arrow.apply_style_string("whiteSpace=wrap;rounded=0;fillColor=#4D4D4D;strokeColor=none;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;strokeWidth=2;shape=mxgraph.arrows2.arrow;dy=0.54;dx=11.29;notch=0;fontStyle=1;direction=north;fontStyle=1;")


file.write()