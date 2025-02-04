import drawpyo
from os import path

base_url = "https://raw.githubusercontent.com/TrivadisPF/arch-diagrams/refs/heads/main/icons/building-blocks/"

file = drawpyo.File()
file.file_path = path.join("./out/")
file.file_name = "Apply_Style_From_String.drawio"
page = drawpyo.Page(file=file)

persistence = drawpyo.diagram.object_from_library(
    page=page,
    library="general",
    obj_name="rounded_rectangle",
    value="Data Persistence Services",
    width=760,
    height=640,
    text_format=drawpyo.diagram.TextFormat(bold=True)
    )
persistence.apply_style_string("whiteSpace=wrap;rounded=1;fillColor=#F0F0F0;strokeColor=default;dashed=0;inherit=default;spacingRight=40;spacingBottom=0;spacingLeft=3;spacingTop=1;html=1;labelBackgroundColor=none;strokeWidth=1;fontColor=default;arcSize=20;absoluteArcSize=1;horizontal=1;verticalAlign=top;align=center;fontStyle=1;fontStyle=1;")
persistence.center_position = (0,0)

graph_db = drawpyo.diagram.object_from_library(
    page=page,
    parent=persistence,
    library="general",
    obj_name="rounded_rectangle",
    value="Graph\nDatabase",
    width=120,
    height=180,
    text_format=drawpyo.diagram.TextFormat(bold=True)
    )
graph_db.apply_style_string("rounded=1;whiteSpace=wrap;whiteSpace=wrap;spacingRight=42;spacingBottom=0;spacingLeft=3;spacingTop=1;html=1;labelBackgroundColor=default;strokeColor=default;strokeWidth=1;fillColor=default;fontColor=default;arcSize=20;absoluteArcSize=1;horizontal=1;verticalAlign=top;align=left;")
graph_db.center_position = (80,120)

image_url = base_url + "persistence" + "/" + "graph-database" + ".png"
style_str_obj = drawpyo.diagram.Object(page=page, parent=graph_db, width=30, height=30)
style_str_obj.apply_style_string(
    "shape=image;verticalLabelPosition=bottom;labelBackgroundColor=none;verticalAlign=top;aspect=fixed;imageAspect=0;image=" + image_url + ";"
)
style_str_obj.center_position = (95,20)

style_str_obj = drawpyo.diagram.Object(page=page, parent=graph_db, width=35, height=35, value="Amazon Neptune", text_format=drawpyo.diagram.TextFormat(size=10))
style_str_obj.apply_style_string("sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.neptune;")
#style_str_obj.center_position = (60,65)
style_str_obj.center_position = (30,65)

style_str_obj = drawpyo.diagram.Object(page=page, parent=graph_db, width=35, height=35, value="Amazon Neptune", text_format=drawpyo.diagram.TextFormat(size=10))
style_str_obj.apply_style_string("sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.neptune;")
#style_str_obj.center_position = (60,65)
style_str_obj.center_position = (90,65)

rdbms = drawpyo.diagram.object_from_library(
    page=page,
    parent=persistence,
    library="general",
    obj_name="rounded_rectangle",
    value="Relational Database",
    width=120,
    height=180,
    text_format=drawpyo.diagram.TextFormat(bold=True)
    )    
rdbms.apply_style_string("rounded=1;whiteSpace=wrap;spacingRight=42;spacingBottom=0;spacingLeft=3;html=1;labelBackgroundColor=default;strokeColor=default;strokeWidth=1;fillColor=default;fontColor=default;arcSize=20;absoluteArcSize=1;horizontal=1;verticalAlign=top;align=left;")
rdbms.center_position = (220,120)

image_url = base_url + "persistence" + "/" + "relational-database" + ".png"
style_str_obj = drawpyo.diagram.Object(page=page, parent=rdbms, width=30, height=30)
style_str_obj.apply_style_string(
    "shape=image;verticalLabelPosition=bottom;labelBackgroundColor=none;verticalAlign=top;aspect=fixed;imageAspect=0;image=" + image_url + ";"
)
style_str_obj.center_position = (95,20)

event_broker = drawpyo.diagram.object_from_library(
    page=page,
    parent=persistence,
    library="general",
    obj_name="rounded_rectangle",
    value="Event Broker",
    width=120,
    height=180,
    text_format=drawpyo.diagram.TextFormat(bold=True)
    )    
event_broker.apply_style_string("rounded=1;whiteSpace=wrap;spacingRight=42;spacingBottom=0;spacingLeft=3;html=1;labelBackgroundColor=default;strokeColor=default;strokeWidth=1;fillColor=default;fontColor=default;arcSize=20;absoluteArcSize=1;horizontal=1;verticalAlign=top;align=left;")
event_broker.center_position = (360,120)

image_url = base_url + "persistence" + "/" + "event-broker" + ".png"
style_str_obj = drawpyo.diagram.Object(page=page, parent=event_broker, width=30, height=30)
style_str_obj.apply_style_string(
    "shape=image;verticalLabelPosition=bottom;labelBackgroundColor=none;verticalAlign=top;aspect=fixed;imageAspect=0;image=" + image_url + ";"
)
style_str_obj.center_position = (95,20)

file.write()