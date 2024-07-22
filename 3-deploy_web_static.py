#!/usr/bin/python3
"""deploy code to servers"""
from fabric.api import *
from datetime import datetime
import os


env.hosts = ["100.25.144.102", "34.207.58.33"]


def do_pack():
    """pack files into a tgz then get from remote servers"""
    # /data/web_static/
    # web_static_<year><month><day><hour><minute><second>.tgz
    try:
        date_time = str(datetime.now()).split(" ")
        date_now = date_time[0].split("-")
        time_now = date_time[1].split(":")
        year, month, day = date_now[0], date_now[1], date_now[2]
        hour, min, sec = time_now[0], time_now[1], int(float(time_now[2]))
        file_name = f"web_static_{year}{month}{day}{hour}{min}{sec}.tgz"
        local("mkdir -p versions")
        local(f"tar -cvzf ./versions/{file_name} -C ./web_static .")
        cwd = os.getcwd()
        return f"{cwd}/versions/{file_name}"
    except Exception:
        return False


def do_deploy(archive_path):
    """deploy code to remote servers"""
    if not os.path.exists(archive_path):
        return False
    put(local_path=archive_path, remote_path="/tmp/")
    archive_name = archive_path.split("/")[-1][:-4]  # without extension
    run(f"mkdir -p /data/web_static/releases/{archive_name}")
    run(f"tar -xvzf /tmp/{archive_name}.tgz" +
        f" -C /data/web_static/releases/{archive_name}")
    run(f"rm -f /tmp/{archive_name}.tgz")
    run(f"rm -rf /data/web_static/current")
    sudo(f"ln -s /data/web_static/releases/{archive_name}" +
         " /data/web_static/current")
    return True


def deploy():
    """deploy all modification to servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
