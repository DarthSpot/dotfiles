import os
from libqtile.lazy import lazy
from libqtile.config import Key

mod = "mod4"
terminal = "kitty"



def resize(qtile, direction):
    layout = qtile.current_layout
    child = layout.current
    parent = child.parent

    while parent:
        if child in parent.children:
            layout_all = False

            if (direction == "left" and parent.split_horizontal) or (
                direction == "up" and not parent.split_horizontal
            ):
                parent.split_ratio = max(5, parent.split_ratio - layout.grow_amount)
                layout_all = True
            elif (direction == "right" and parent.split_horizontal) or (
                direction == "down" and not parent.split_horizontal
            ):
                parent.split_ratio = min(95, parent.split_ratio + layout.grow_amount)
                layout_all = True

            if layout_all:
                layout.group.layout_all()
                break

        child = parent
        parent = child.parent


@lazy.function
def resize_left(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "left")
    elif current == "columns":
        layout.cmd_grow_left()


@lazy.function
def resize_right(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "right")
    elif current == "columns":
        layout.cmd_grow_right()


@lazy.function
def resize_up(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "up")
    elif current == "columns":
        layout.cmd_grow_up()


@lazy.function
def resize_down(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "down")
    elif current == "columns":
        layout.cmd_grow_down()


def show_keys():
    key_help = ""
    for k in keys:
        mods = ""

        for m in k.modifiers:
            if m == "mod4":
                mods += "Super + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            mods += k.key.capitalize()
        else:
            mods += k.key

        key_help += "{:<30} {}".format(mods, k.desc + "\n")

    return key_help


# Padding
def padding(qtile, direction):
    if direction == "+":
        qtile.current_screen.left.size += 18
        qtile.current_screen.top.size += 9
        qtile.current_screen.right.size += 18
        qtile.current_screen.bottom.size += 9
        qtile.current_group.layout_all()
    elif direction == "-":
        qtile.current_screen.left.size -= 18
        qtile.current_screen.top.size -= 9
        qtile.current_screen.right.size -= 18
        qtile.current_screen.bottom.size -= 9
        qtile.current_group.layout_all()
    else:
        qtile.current_screen.left.size = 18
        qtile.current_screen.top.size = 77
        qtile.current_screen.right.size = 18
        qtile.current_screen.bottom.size = 18
        qtile.current_layout.margin = 9
        qtile.current_group.layout_all()


@lazy.function
def inc_pad(qtile):
    padding(qtile, "+")


@lazy.function
def dec_pad(qtile):
    padding(qtile, "-")


@lazy.function
def reset_pad(qtile):
    padding(qtile, "reset")


@lazy.function
def inc_margins(qtile):
    qtile.current_layout.margin += 9
    qtile.current_group.layout_all()


@lazy.function
def dec_margins(qtile):
    qtile.current_layout.margin -= 9
    qtile.current_group.layout_all()

keys = [
    # The essentials
    Key([mod], "Return", lazy.spawn(terminal), desc="Launches My Terminal"),
    Key(
        [mod],
        "d",
        lazy.spawn("rofi -show drun -show-icons"),
        desc="Rofi app launcher",
    ),
    Key([mod], "w", lazy.spawn("firefox"), desc="Firefox"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle forward layout"),
    Key([mod, "shift"], "Tab", lazy.prev_layout(), desc="Toggle last layout"),
    Key([mod], "q", lazy.window.kill(), desc="Kill active window"),
    Key(
        [mod, "shift"],
        "r",
        lazy.restart(),
        # lazy.spawn("reopen_eww.sh"),
        desc="Restart Qtile",
    ),
    Key(
        [mod, "shift"],
        "e",
        lazy.spawn(os.path.expanduser('~/.config/rofi/scripts/powermenu.sh')),
        desc="Power Menu",
    ),
    # Switch focus to specific monitor (out of three)
    # Key([mod], "w", lazy.to_screen(0), desc="Keyboard focus to monitor 1"),
    # Key([mod], "e", lazy.to_screen(1), desc="Keyboard focus to monitor 2"),
    # Key([mod], "r", lazy.to_screen(2), desc="Keyboard focus to monitor 3"),
    # Switch focus of monitors
    # Key([mod], "period", lazy.next_screen(), desc="Move focus to next monitor"),
    # Key([mod], "comma", lazy.prev_screen(), desc="Move focus to prev monitor"),
    # Window controls
    # Change Focus
    Key(
        [mod], "Down", lazy.layout.down(), desc="Move focus down in current stack pane"
    ),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up in current stack pane"),
    Key(
        [mod],
        "Left",
        lazy.layout.left(),
        # lazy.layout.next(),
        desc="Move focus left in current stack pane",
    ),
    Key(
        [mod],
        "Right",
        lazy.layout.right(),
        # lazy.layout.previous(),
        desc="Move focus right in current stack pane",
    ),
    # Move windows within group
    Key(
        [mod, "shift"],
        "Down",
        lazy.layout.shuffle_down(),
        lazy.layout.move_down(),
        desc="Move windows down in current stack",
    ),
    Key(
        [mod, "shift"],
        "Up",
        lazy.layout.shuffle_up(),
        lazy.layout.move_up(),
        desc="Move windows up in current stack",
    ),
    Key(
        [mod, "shift"],
        "Left",
        lazy.layout.shuffle_left(),
        # lazy.layout.swap_left(),
        # lazy.layout.client_to_previous(),
        lazy.layout.move_left(),
        desc="Move windows left in current stack",
    ),
    Key(
        [mod, "shift"],
        "Right",
        lazy.layout.shuffle_right(),
        # lazy.layout.swap_right(),
        # lazy.layout.client_to_next(),
        lazy.layout.move_right(),
        desc="Move windows right in the current stack",
    ),
    # Flip layouts for bsp
    Key(
        [mod, "control"],
        "Down",
        lazy.layout.flip_down(),
        # lazy.layout.section_down(),
        # lazy.layout.integrate_down(),
        desc="Flip layout down",
    ),
    Key(
        [mod, "control"],
        "Up",
        lazy.layout.flip_up(),
        # lazy.layout.section_up(),
        # lazy.layout.integrate_up(),
        desc="Flip layout up",
    ),
    Key(
        [mod, "control"],
        "Left",
        lazy.layout.flip_left(),
        lazy.layout.swap_column_left(),
        # lazy.layout.integrate_left(),
        desc="Flip layout left",
    ),
    Key(
        [mod, "control"],
        "Right",
        lazy.layout.flip_right(),
        lazy.layout.swap_column_left(),
        # lazy.layout.integrate_right(),
        desc="Flip layout right",
    ),
    # Resize windows
    Key(
        [mod, "mod1"],
        "Left",
        resize_left,
        # lazy.layout.grow_width(-30),
        desc="Resize window left",
    ),
    Key(
        [mod, "mod1"],
        "Right",
        resize_right,
        # lazy.layout.grow_width(30),
        desc="Resize window Right",
    ),
    Key(
        [mod, "mod1"],
        "Up",
        resize_up,
        # lazy.layout.grow_height(30),
        desc="Resize windows upward",
    ),
    Key(
        [mod, "mod1"],
        "Down",
        resize_down,
        # lazy.layout.grow_height(-30),
        desc="Resize windows downward",
    ),
    Key(
        [mod],
        "n",
        lazy.layout.normalize(),
        # lazy.layout.reset_size(),
        desc="Normalize window size ratios",
    ),
    # Window States
    Key(
        [mod],
        "m",
        lazy.window.toggle_maximize(),
        desc="Toggle window between minimum and maximum sizes",
    ),
    Key([mod, "shift"], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on focused window",
    ),
    Key(
        [mod],
        "h",
        lazy.window.toggle_minimize(),
        desc="Toggle minimization on focused window",
    ),
    Key(
        [mod, "shift"],
        "h",
        lazy.group.unminimize_all(),
        desc="Unminimize all windows on current group",
    ),
    # Adjust paddings/margins
    Key([mod, "mod1"], "equal", reset_pad, desc="Reset padding"),
    Key([mod], "minus", dec_pad, desc="Decrease padding"),
    Key([mod], "equal", inc_pad, desc="Increase padding"),
    Key([mod, "shift"], "minus", dec_margins, desc="Decrease layout margins"),
    Key([mod, "shift"], "equal", inc_margins, desc="Increase layout margins"),
    # Plasma controls
    # Key(
    # 	[mod],
    # 	"o",
    # 	lazy.layout.mode_horizontal(),
    # 	desc="Horizontal Mode in Plasma Layout",
    # ),
    # Key(
    # 	[mod, "shift"],
    # 	"o",
    # 	lazy.layout.mode_horizontal_split(),
    # 	desc="Horizontal Split mode in Plasma Layout",
    # ),
    # Key(
    # 	[mod],
    # 	"u",
    # 	lazy.layout.mode_vertical(),
    # 	desc="Vertical Mode in Plasma Layout",
    # ),
    # Key(
    # 	[mod, "shift"],
    # 	"u",
    # 	lazy.layout.mode_vertical_split(),
    # 	desc="Vertical Split Mode in Plasma Layout",
    # ),
    # Split direction in Bsp/ Split stack in columns
    Key(
        [mod],
        "s",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Floating controls
    Key(
        [mod],
        "bracketleft",
        lazy.group.prev_window(),
        lazy.window.bring_to_front(),
        desc="Cycle previous floating window",
    ),
    Key(
        [mod],
        "bracketright",
        lazy.group.next_window(),
        lazy.window.bring_to_front(),
        desc="Cycle next floating windows",
    ),
    # TreeTab controls
    # Key(
    # 	[mod],
    # 	"v",
    # 	lazy.layout.expand_branch(),
    # 	desc="Expand a branch in the treetab panel",
    # ),
    # Key(
    # 	[mod, "shift"],
    # 	"v",
    # 	lazy.layout.collapse_branch(),
    # 	desc="Collapse a branch in the treetab panel",
    # ),
    ### Misc. Commands
    Key(
        [mod],
        "b",
        lazy.spawn("./.config/qtile/toggle_eww.sh"),
        desc="Toggle bottom eww bar visibility",
    ),
    Key(
        [mod, "shift"],
        "b",
        lazy.spawn("toggle_qbar.sh"),
        desc="Toggle visibility of qtile bar",
    ),
    Key(
        [mod],
        "n",
        lazy.spawn("thunar"),
        desc="Launch Thunar",
    ),
    Key(
        [mod, "shift"],
        "d",
        lazy.spawn(
            "rofi -theme ~/.config/rofi/configTall.rasi -show window -window-format '{c} {t}' -window-thumbnail"
        ),
        desc="Rofi window select",
    ),
    Key(
        [mod],
        "space",
        lazy.spawn("rofi_notes.sh"),
        desc="Rofi quick notes",
    ),
    Key(
        [],
        "Print",
        lazy.spawn("flameshot gui"),
        desc="Print Screen",
    ),
    Key(
        [],
        "XF86AudioRaiseVolume",
        lazy.spawn("sh ./.config/qtile/eww_vol.sh up"),
        desc="Increase mic volume",
    ),
    Key(
        [],
        "XF86AudioLowerVolume",
        lazy.spawn("sh ./.config/qtile/eww_vol.sh down"),
        #lazy.spawn("amixer set Master 3%-"),
        desc="Decrease mic volume",
    ),
    Key(
        [],
        "XF86AudioMute",
        lazy.spawn("sh ./.config/qtile/eww_vol.sh mute"),
        desc="Toggle mic mute",
    ),
    Key(
        [mod],
        "F7",
        lazy.spawn("playerctl previous"),
        desc="Play last audio",
    ),
    Key([mod], "F8", lazy.spawn("playerctl next"), desc="Play next audio"),
    Key(
        [mod], "F5", lazy.spawn("playerctl play-pause"), desc="Toggle play/pause audio"
    ),
    Key([mod], "F6", lazy.spawn("playerctl stop"), desc="Stop audio"),
    Key(
        [mod],
        "z",
        lazy.spawn(
            "rofi -show file-browser-extended -file-browser-show-hidden -theme ~/.config/rofi/configTall.rasi -file-browser-cmd 'xdg-open'"
        ),
        desc="Rofi find files",
    ),
    Key(
        [mod, "shift"],
        "z",
        lazy.spawn("rofi-search.sh"),
        desc="Rofi google search",
    ),
    Key(
        [mod, "control"],
        "r",
        lazy.spawn("mp4"),
        desc="Record selected part of screen in mp4",
    ),
    Key(
        [mod, "control", "shift"],
        "r",
        lazy.spawn("gif"),
        desc="Record selected part of screen as gif",
    ),
    Key(
        [mod, "shift"],
        "p",
        lazy.spawn("togglepicom"),
        desc="Toggle picom",
    ),
    Key([mod], "x", lazy.spawn("greenclip.sh"), desc="Greenclip"),
    Key([mod, "shift"], "c", lazy.spawn("colorpick.sh"), desc="Color picker"),
    Key(
        [mod, "control"],
        "c",
        lazy.spawn("toggledunst"),
        desc="Toggle dunst",
    ),
    Key(
        [mod, "mod1"],
        "c",
        lazy.spawn(
            "sh -c 'xdotool mousemove --window \"$(xdotool getwindowfocus)\" --polar 0 0'"
        ),
        desc="Teleport cursor to center of focused window",
    ),
    Key(
        [mod],
        "grave",
        lazy.spawn("rofi_notif_center.sh"),
        desc="Open notification center",
    ),
    Key(
        [],
        "XF86Calculator",
        lazy.spawn("io.elementary.calculator"),
        desc="Launch calculator",
    ),
]

keys.extend(
    [
        Key(
            [mod],
            "a",
            lazy.spawn(
                "sh -c 'echo \""
                + show_keys()
                + '" | rofi -dmenu -theme ~/.config/rofi/configTall.rasi -i -p "?"\''
            ),
            desc="Print keyboard bindings",
        ),
    ]
)
