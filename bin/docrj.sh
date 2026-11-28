import png:-|tesseract stdin stdout -l jpn_vert --psm 3 --dpi 500|tr -d  |mecab|awk {print }|xargs sdcv -n -e -u EDICT
