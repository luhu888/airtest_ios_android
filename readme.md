如果ios报错  Poco报错：TypeError: string indices must be integers
在中poco/drivers/ios/__init__.py，我这样修改：
    # w = float(node["frame"]["width"])
    # h = float(node["frame"]["height"])
    # x = float(node["frame"]["x"])
    # y = float(node["frame"]["y"])

    w = float(node["rect"]["width"])
    h = float(node["rect"]["height"])
    x = float(node["rect"]["x"])
    y = float(node["rect"]["y"])