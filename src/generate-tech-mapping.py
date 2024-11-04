import drawpyo
from os import path

file = drawpyo.File()
file.file_path = path.join("/data-transfer/")
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

item = drawpyo.diagram.object_from_library(
    page=page,
    parent=persistence,
    library="general",
    obj_name="rounded_rectangle",
    value="Graph\nDatabase",
    width=120,
    height=180,
    text_format=drawpyo.diagram.TextFormat(bold=True)
    )
item.apply_style_string("rounded=1;whiteSpace=wrap;whiteSpace=wrap;spacingRight=40;spacingBottom=0;spacingLeft=3;spacingTop=1;html=1;labelBackgroundColor=default;strokeColor=default;strokeWidth=1;fillColor=default;fontColor=default;arcSize=20;absoluteArcSize=1;horizontal=1;verticalAlign=top;align=left;")
item.center_position = (80,120)

style_str_obj = drawpyo.diagram.Object(page=page, parent=item, width=30, height=30)
style_str_obj.apply_style_string(
    "shape=image;verticalLabelPosition=bottom;labelBackgroundColor=none;verticalAlign=top;aspect=fixed;imageAspect=0;image=data:image/png,iVBORw0KGgoAAAANSUhEUgAAACAAAAAhCAYAAAC4JqlRAAACs0lEQVRYCb2XS6iOQRzGfyW5JEWinEKKyEKxIukUSsLCJeUSKcplocghdxYuC2KpFDY2KAtRWChsKKzExmVD7FySKHrOmXn9z3zzvjPz5fOvr7l8zzz/Z+aded55ofMxB7gBfAF+APeBlZ1P25dhBfC75rc7FLEAuAV8A74Dd4HFIaigPQB4X5Pci5rm+TY0ALd5UGG5vIHTCzgkzhHA1wR4XGFywXckOCXigoAbM4AiK41VGbxHRXo4A3i6NDswJGNlZ4h3U4aAXW0ImA38auA+4jnHJIB6VpM8OLMcD7xxyW+7s+833nP32PtRaad7QKzc2Q/d3BgIPHJ8Nw10EDDMtFuqOjZ+oEQ8Bi4ZYS3G0cLQ13HVjXkKDK/BNHZr8ww1iO1GxF7TH6uec9iPwNQYoN2+LUbEfkDLuRY4COg/PfM9BjMvSLTEOascVk4rx50fYJLNzSaBXiyxvaK+dQGTXcFwzPoAm2zKOEIS274WMGhl7P9hXRMpissJwlfAWEAGswi4ksBLUFG8ziAMZ5lqFwl4myHgE/AMkAHpKP9TAakllfvZmJwQ8NOCc+rHEoQPIiQysLpV2BrB13ZZu5byOtJ7QFfAsgZ4YsbIcZcFmKo5EVAymcxqQFcrOwsZ0WhA5/sMIHecDswCdAokTHulu2L8W5HDymlr44BR6Wf42fSlLiajAL2A/Fi96rOjybFEqBXJjbNGxEk3SPYsu+4B5saI3plBfga2PB8b1NBnJ/Qhwn0dGOzHp46LhLzw4IJyofsYsROxdYnojSkRhRao+ksPLiiXZvBWdLFlsiIuVsj8yvESAbp42oRhfWZ+3gqpDRjyhO0KrMqpyAAdQ93x24mcr6MWXr1K9zmTkVWObEGUdTyMTMqvgm5GHY8JQEzEHUDG9d9Cj+MEoI2p09EbfwDef7qD2iGWzgAAAABJRU5ErkJggg==;"
)
style_str_obj.center_position = (95,20)

style_str_obj = drawpyo.diagram.Object(page=page, parent=item, width=35, height=35, value="Amazon Neptune", text_format=drawpyo.diagram.TextFormat(size=10))
style_str_obj.apply_style_string("sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.neptune;")
#style_str_obj.center_position = (60,65)
style_str_obj.center_position = (30,65)

style_str_obj = drawpyo.diagram.Object(page=page, parent=item, width=35, height=35, value="Amazon Neptune", text_format=drawpyo.diagram.TextFormat(size=10))
style_str_obj.apply_style_string("sketch=0;points=[[0,0,0],[0.25,0,0],[0.5,0,0],[0.75,0,0],[1,0,0],[0,1,0],[0.25,1,0],[0.5,1,0],[0.75,1,0],[1,1,0],[0,0.25,0],[0,0.5,0],[0,0.75,0],[1,0.25,0],[1,0.5,0],[1,0.75,0]];outlineConnect=0;fontColor=#232F3E;fillColor=#C925D1;strokeColor=#ffffff;dashed=0;verticalLabelPosition=bottom;verticalAlign=top;align=center;html=1;fontSize=10;fontStyle=0;aspect=fixed;shape=mxgraph.aws4.resourceIcon;resIcon=mxgraph.aws4.neptune;")
#style_str_obj.center_position = (60,65)
style_str_obj.center_position = (90,65)

item2 = drawpyo.diagram.object_from_library(
    page=page,
    parent=persistence,
    library="general",
    obj_name="rounded_rectangle",
    value="RDBMS",
    width=120,
    height=180,
    text_format=drawpyo.diagram.TextFormat(bold=True)
    )
item2.apply_style_string("rounded=1;whiteSpace=wrap;spacingRight=40;spacingBottom=0;spacingLeft=3;html=1;labelBackgroundColor=default;strokeColor=default;strokeWidth=1;fillColor=default;fontColor=default;arcSize=20;absoluteArcSize=1;horizontal=1;verticalAlign=top;align=left;")
item2.center_position = (220,120)

style_str_obj = drawpyo.diagram.Object(page=page, parent=item2, width=30, height=30)
style_str_obj.apply_style_string(
    "shape=image;verticalLabelPosition=bottom;labelBackgroundColor=none;verticalAlign=top;aspect=fixed;imageAspect=0;image=https://cdn.iconscout.com/icon/premium/png-256-thumb/relational-database-2417343-2036435.png;"
)
style_str_obj.center_position = (95,20)


file.write()