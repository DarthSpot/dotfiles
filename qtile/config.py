# -*- coding: utf-8 -*-
import os
import subprocess
from typing import List  # noqa: F401
import psutil

from libqtile.config import (
    Key,
    Screen,
    Group,
    Drag,
    Click,
    ScratchPad,
    DropDown,
    Match,
)
from libqtile import layout, bar, widget, hook
from libqtile import qtile
from libqtile.lazy import lazy
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.widget.decorations import RectDecoration
from modules.keys import keys, mod

# from plasma import Plasma


mod = "mod4"
terminal = "kitty"

# Resize functions for bsp layout

workspaces = [
    {"name": "", "key": "1", "matches": [Match(wm_class="firefox")], "lay": "bsp"},
    {"name": "", "key": "2", "matches": [Match(wm_class="kitty")], "lay": "bsp"},
    {"name": "", "key": "3", "matches": [Match(wm_class="kate")], "lay": "bsp"},
    {
        "name": "",
        "key": "4",
        "matches": [
            Match(wm_class="slack"),
            Match(wm_class="discord"),
        ],
        "lay": "bsp",
    },
    {
        "name": "",
        "key": "5",
        "matches": [Match(wm_class="vlc")],
        "lay": "bsp",
    },
    {
        "name": "",
        "key": "6",
        "matches": [Match(wm_class="Thunar")],
        "lay": "bsp",
    },
    {
        "name": "",
        "key": "7",
        "matches": [
            Match(wm_class="lxappearance"),
            Match(wm_class="pavucontrol"),
        ],
        "lay": "floating",
    },
]

groups = [
    ScratchPad(
        "scratchpad",
        [
            # define a drop down terminal.
            DropDown(
                "term",
                "alacritty --class dropdown -e tmux new -As Dropdown",
                height=0.6,
                on_focus_lost_hide=False,
                opacity=1,
                warp_pointer=False,
            ),
        ],
    ),
]

for workspace in workspaces:
    matches = workspace["matches"] if "matches" in workspace else None
    groups.append(Group(workspace["name"], matches=matches, layout=workspace["lay"]))
    keys.append(
        Key(
            [mod],
            workspace["key"],
            lazy.group[workspace["name"]].toscreen(toggle=True),
            desc="Focus this desktop",
        )
    )
    keys.append(
        Key(
            [mod, "shift"],
            workspace["key"],
            lazy.window.togroup(workspace["name"]),
            desc="Move focused window to another group",
        )
    )

# Define colors

colors = [
    ["#2e3440", "#2e3440"],  # 0 background
    ["#d8dee9", "#d8dee9"],  # 1 foreground
    ["#3b4252", "#3b4252"],  # 2 background lighter
    ["#bf616a", "#bf616a"],  # 3 red
    ["#a3be8c", "#a3be8c"],  # 4 green
    ["#ebcb8b", "#ebcb8b"],  # 5 yellow
    ["#81a1c1", "#81a1c1"],  # 6 blue
    ["#b48ead", "#b48ead"],  # 7 magenta
    ["#88c0d0", "#88c0d0"],  # 8 cyan
    ["#e5e9f0", "#e5e9f0"],  # 9 white
    ["#4c566a", "#4c566a"],  # 10 grey
    ["#d08770", "#d08770"],  # 11 orange
    ["#8fbcbb", "#8fbcbb"],  # 12 super cyan
    ["#5e81ac", "#5e81ac"],  # 13 super blue
    ["#242831", "#242831"],  # 14 super dark background
]

layout_theme = {
    "border_width": 3,
    "margin": 9,
    "border_focus": "bf616a",
    "border_normal": "3b4252",
    "font": "FiraCode Nerd Font",
    "grow_amount": 2,
}

layouts = [
    # layout.MonadWide(**layout_theme),
    layout.Bsp(**layout_theme, fair=False, border_on_single=True),
    layout.Columns(
        **layout_theme,
        border_on_single=True,
        num_columns=2,
        border_focus_stack="#3b4252",
        border_normal_stack="#3b4252",
        split=False,
        wrap_focus_columns=True,
        wrap_focus_rows=True,
        wrap_focus_stacks=True,
    ),
    # Plasma(**layout_theme, border_normal_fixed='#3b4252', border_focus_fixed='#3b4252', border_width_single=3),
    # layout.RatioTile(**layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme, columns=3),
    # layout.Zoomy(**layout_theme),
    # layout.Slice(**layout_theme, width=1920, fallback=layout.TreeTab(), match=Match(wm_class="joplin"), side="right"),
    # layout.MonadTall(**layout_theme),
    # layout.Max(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.Stack(num_stacks=2, **layout_theme),
    layout.Floating(**layout_theme),
]

# Setup bar

widget_defaults = dict(
    font="FiraCode Nerd Font",
    fontsize=14,
    padding=2,
    background=colors[0],
    decorations=[
        BorderDecoration(
            colour=colors[0],
            border_width=[11, 0, 10, 0],
        )
    ],
)
extension_defaults = widget_defaults.copy()

group_box_settings = {
    "padding": 5,
    "borderwidth": 4,
    "active": colors[9],
    "inactive": colors[10],
    "disable_drag": True,
    "rounded": True,
    "highlight_color": colors[2],
    "block_highlight_text_color": colors[6],
    "highlight_method": "block",
    "this_current_screen_border": colors[14],
    "this_screen_border": colors[7],
    "other_current_screen_border": colors[14],
    "other_screen_border": colors[14],
    "foreground": colors[1],
    "background": colors[14],
    "urgent_border": colors[3],
}

# Define functions for bar


def dunst():
    return subprocess.check_output(["./.config/qtile/dunst.sh"]).decode("utf-8").strip()


def toggle_dunst():
    qtile.cmd_spawn("./.config/qtile/dunst.sh --toggle")


def toggle_notif_center():
    qtile.cmd_spawn("./.config/qtile/dunst.sh --notif-center")


# Mouse_callback functions
def open_launcher():
    qtile.cmd_spawn("rofi -show drun -show-icons")


def kill_window():
    qtile.cmd_spawn("xdotool getwindowfocus windowkill")


def open_pavu():
    qtile.cmd_spawn("pavucontrol")


def open_powermenu():
    qtile.cmd_spawn(os.path.expanduser('~/.config/rofi/powermenu.sh')),


screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(
                    filename='~/.config/qtile/eos-c.png', 
                    mouse_callbacks={'Button1': lambda: qtile.cmd_spawn("rofi -show combi")},
                    padding=20,
                    scale=True,
                    margin=6,
                    foreground=colors[13],
                    background=colors[0],
                    ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=21,
                    padding=0,
                ),
                widget.GroupBox(
                    font="Font Awesome 6 Brands",
                    visible_groups=[""],
                    **group_box_settings,
                ),
                widget.GroupBox(
                    font="Font Awesome 6 Free Solid",
                    visible_groups=["", "", "", "", "", "", "", "", ""],
                    **group_box_settings,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=21,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    background=colors[0],
                    padding=10,
                    size_percent=40,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=21,
                    padding=0,
                ),
                widget.CurrentLayoutIcon(
                    custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
                    foreground=colors[2],
                    background=colors[14],
                    padding=-10,
                    scale=0.40,
                ),
                widget.WindowCount(
                    background=colors[14],
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=21,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=21,
                    padding=0,
                ),
                widget.GenPollText(
                    func=dunst,
                    update_interval=1,
                    foreground=colors[11],
                    background=colors[14],
                    padding=8,
                    mouse_callbacks={
                        "Button1": toggle_dunst,
                        "Button3": toggle_notif_center,
                    },
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=21,
                    padding=0,
                ),
                widget.Spacer(),
                widget.TextBox(
                    text=" ",
                    foreground=colors[12],
                    background=colors[0],
                    # fontsize=38,
                    font="Font Awesome 6 Free Solid",
                ),
                widget.WindowName(
                    background=colors[0],
                    foreground=colors[12],
                    width=bar.CALCULATED,
                    empty_group_string="Desktop",
                    max_chars=20,
                    mouse_callbacks={"Button2": kill_window},
                ),
                widget.Spacer(),
                widget.Systray(
                    icon_size=26,
                    background=colors[0],
                    padding=7,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=21,
                    padding=0,
                ),
                widget.TextBox(
                    text=" ",
                    foreground=colors[8],
                    background=colors[14],
                    font="Font Awesome 6 Free Solid",
                    # fontsize=38,
                ),
                widget.PulseVolume(
                    foreground=colors[8],
                    background=colors[14],
                    limit_max_volume="True",
                    mouse_callbacks={"Button3": open_pavu},
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=21,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=21,
                    padding=0,
                ),
                widget.Battery(
                    foreground=colors[7],
                    background=colors[14],
                    padding=5,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=21,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=21,
                    padding=0,
                ),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    foreground=colors[5],  # fontsize=38
                    background=colors[14],
                ),
                widget.Clock(
                    format="%a, %b %d",
                    background=colors[14],
                    foreground=colors[5],
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=21,
                    padding=0,
                ),
                widget.Sep(
                    linewidth=0,
                    foreground=colors[2],
                    padding=10,
                    size_percent=50,
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=21,
                    padding=0,
                ),
                widget.TextBox(
                    text=" ",
                    font="Font Awesome 6 Free Solid",
                    foreground=colors[4],  # fontsize=38
                    background=colors[14],
                ),
                widget.Clock(
                        format="%H:%M:%S",
                    foreground=colors[4],
                    background=colors[14],
                ),
                widget.TextBox(
                    text="",
                    foreground=colors[14],
                    background=colors[0],
                    fontsize=21,
                    padding=0,
                ),
                widget.TextBox(
                    text="⏻",
                    foreground=colors[13],
                    font="Font Awesome 6 Free Solid",
                    fontsize=26,
                    padding=20,
                    mouse_callbacks={"Button1": open_powermenu},
                ),
            ],
            44,
            margin=[0, 0, 21, 0],
            border_width=[0, 0, 3, 0],
            border_color="#3b4252",
        ),
        bottom=bar.Gap(18),
        left=bar.Gap(18),
        right=bar.Gap(18),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = "floating_only"
cursor_warp = False
floating_layout = layout.Floating(
    **layout_theme,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(title="pinentry"),  # GPG key password entry
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="pomotroid"),
        Match(wm_class="cmatrixterm"),
        Match(title="Farge"),
        Match(wm_class="thunar"),
        Match(wm_class="feh"),
        Match(wm_class="eog"),
        Match(wm_class="io.elementary.calculator"),
        Match(wm_class="blueberry.py"),
    ],
)
auto_fullscreen = True
focus_on_window_activation = "focus"

# Startup scripts


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/autostart.sh"])


# Window swallowing ;)
@hook.subscribe.client_new
def _swallow(window):
    pid = window.window.get_net_wm_pid()
    ppid = psutil.Process(pid).ppid()
    cpids = {
        c.window.get_net_wm_pid(): wid for wid, c in window.qtile.windows_map.items()
    }
    for i in range(5):
        if not ppid:
            return
        if ppid in cpids:
            parent = window.qtile.windows_map.get(cpids[ppid])
            parent.minimized = True
            window.parent = parent
            return
        ppid = psutil.Process(ppid).ppid()


@hook.subscribe.client_killed
def _unswallow(window):
    if hasattr(window, "parent"):
        window.parent.minimized = False


# Go to group when app opens on matched group
@hook.subscribe.client_new
def modify_window(client):
    # if (client.window.get_wm_transient_for() or client.window.get_wm_type() in floating_types):
    #    client.floating = True

    for group in groups:  # follow on auto-move
        match = next((m for m in group.matches if m.compare(client)), None)
        if match:
            targetgroup = client.qtile.groups_map[
                group.name
            ]  # there can be multiple instances of a group
            targetgroup.cmd_toscreen(toggle=False)
            break


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "qtile"
