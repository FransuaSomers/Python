import psutil
import pystray
import sys
from PIL import Image, ImageDraw, ImageFont
import threading

def get_battery_percent():
    battery = psutil.sensors_battery()
    if battery:
        return battery.percent
    else:
        return None


def get_icon(battery_percent):
    if battery_percent is None:
        return None
    else:
        icon_size = (32, 16)
        icon_padding = 4
        icon_width = icon_size[0] - 2 * icon_padding
        icon_height = icon_size[1] - 2 * icon_padding

        icon = Image.new("RGBA", icon_size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(icon)

        # draw battery outline
        battery_outline = [(0, 0), (icon_width, 0), (icon_width, icon_height), (0, icon_height), (0, 0)]
        draw.line(battery_outline, fill="black", width=1)

        # calculate battery fill size
        fill_width = round(icon_width * battery_percent / 100)
        fill_height = icon_height - 2 * icon_padding

        # calculate battery fill coordinates
        x1 = icon_padding
        y1 = icon_padding
        x2 = icon_padding + fill_width
        y2 = icon_height - icon_padding

        # create battery fill tuple
        battery_fill = [(x1, y1), (x2, y2)]

        # draw battery fill
        draw.rectangle(battery_fill, fill="white")

        battery_fill = [(x1, y1), (x2, y2)]

        # draw battery fill
        battery_fill = [(icon_padding, icon_padding), (icon_padding + fill_width, icon_padding + fill_height)]
        draw.rectangle(battery_fill, fill="white")

        # add text label
        label = "{:3d}%".format(battery_percent)
        label_size = draw.textsize(label)
        label_pos = ((icon_size[0] - label_size[0]) // 2, (icon_size[1] - label_size[1]) // 2)
        draw.text(label_pos, label, fill="black")

        return icon


def get_icon(battery_percent):
    if battery_percent is None:
        return None
    else:
        icon_size = (32, 16)
        icon_padding = 4
        icon_width = icon_size[0] - 2 * icon_padding
        icon_height = icon_size[1] - 2 * icon_padding

        icon = Image.new("RGBA", icon_size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(icon)

        # draw battery outline
        battery_outline = [(0, 0), (icon_width, 0), (icon_width, icon_height), (0, icon_height), (0, 0)]
        draw.line(battery_outline, fill="black", width=1)

        # calculate battery fill size
        fill_width = round(icon_width * battery_percent / 100)
        fill_height = icon_height - 2 * icon_padding

        # draw battery fill
        battery_fill = [(icon_padding, icon_padding), (icon_padding + fill_width, icon_padding + fill_height)]
        draw.rectangle(battery_fill, fill="white")

        # add text label
        label = "{:3d}%".format(battery_percent)
        label_bbox = draw.textbbox((0, 0), label, font=ImageFont.truetype("impact.ttf", 10))
        label_width = label_bbox[2] - label_bbox[0]
        label_height = label_bbox[3] - label_bbox[1]
        label_pos = ((icon_size[0] - label_width) // 2, (icon_size[1] - label_height) // 2)
        draw.text(label_pos, label, fill="black", font=ImageFont.truetype("impact.ttf", 10))

        return icon




def main():
    icon = pystray.Icon("battery")

    # define a function to be called when the dropdown is clicked
    def menu_exit(icon):
        icon.stop()
        sys.exit()

    # create a menu
    menu = (pystray.MenuItem("Exit", menu_exit),)

    # set the menu to the icon
    icon.menu = menu
    
    def update_icon():
        battery_percent = get_battery_percent()
        icon.icon = get_icon(battery_percent)
        icon.title = "Battery: {}%".format(battery_percent) if battery_percent is not None else "Battery: Unknown"
        
    update_icon()
    timer = threading.Timer(60, update_icon)
    timer.start()
    
    icon.run()


if __name__ == "__main__":
    main()
