#!/usr/bin/python3
"""this file is a fabfile togenerate tgz archives"""
from fabric.api import *
from datetime import datetime
import os


def do_pack():
    """pack files into a tgz then get from remote servers"""
    # /data/web_static/
    # web_static_<year><month><day><hour><minute><second>.tgz
    date_time = str(datetime.now()).split(" ")
    date_now = date_time[0].split("-")
    time_now = date_time[1].split(":")
    year, month, day = date_now[0], date_now[1], date_now[2]
    hour, min, sec = time_now[0], time_now[1], int(float(time_now[2]))
    file_name = f"web_static_{year}{month}{day}{hour}{min}{sec}.tgz"
    local("mkdir -p versions")
    local(f"tar -czf ./versions/{file_name} -C ./web_static .")
    home_dir = os.path.expanduser("~")
    if os.path.exists(f"{home_dir}/AirBnB_clone_v2/versions/{file_name}"):
        return f"{home_dir}/AirBnB_clone_v2/versions/{file_name}"
    else:
        return None