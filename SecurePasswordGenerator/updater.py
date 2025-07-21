import socket as dsocket
from asyncio import sleep, new_event_loop, run, gather, create_task, set_event_loop
from contextlib import suppress
from dataclasses import dataclass
from json import load
from os import path, getcwd, listdir, chdir, remove, system, mkdir
from os.path import exists
from random import choice, randrange
from re import findall
from shutil import copytree, rmtree, copyfile
from ssl import create_default_context
from sys import exit
from typing import IO
from urllib.parse import urlparse
from zipfile import ZipFile

from aiohttp import ClientSession
from requests import get


class AutoUpdater:
    def __init__(self, version):
        self.version = version
        self.latest = self.get_latest()
        self.this = getcwd()
        self.file = "temp/latest.zip"
        self.folder = f"temp/latest_{randrange(1_000_000, 999_999_999)}"

    @dataclass
    class latest_data:
        version: str
        zip_url: str

    def get_latest(self):
        rjson = get("https://api.github.com/repos/Jules-Recode/SecurePasswordGenerator/tags").json()
        return self.latest_data(version=rjson[0]["name"], zip_url=get(rjson[0]["zipball_url"]).url)

    @staticmethod
    def download(host, dPath, filename):
        with dsocket.socket(dsocket.AF_INET, dsocket.SOCK_STREAM) as sock:
            context = create_default_context()
            with context.wrap_socket(sock, server_hostname="api.github.com") as wrapped_socket:
                wrapped_socket.connect((dsocket.gethostbyname(host), 443))
                wrapped_socket.send(
                    f"GET {dPath} HTTP/1.1\r\nHost:{host}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,file/avif,file/webp,file/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\n\r\n".encode())

                resp = b""
                while resp[-4:-1] != b"\r\n\r":
                    resp += wrapped_socket.recv(1)
                else:
                    resp = resp.decode()
                    content_length = int(
                        "".join([tag.split(" ")[1] for tag in resp.split("\r\n") if "content-length" in tag.lower()]))
                    _file = b""
                    while content_length > 0:
                        data = wrapped_socket.recv(2048)
                        if not data:
                            print("EOF")
                            break
                        _file += data
                        content_length -= len(data)
                    with open(filename, "wb") as file:
                        file.write(_file)

    def update(self):
        if not self.version == self.latest.version:
            rmtree("temp") if exists("temp") else ""
            mkdir("temp")
            print("Updating Script...")
            parsed = urlparse(self.latest.zip_url)
            self.download(parsed.hostname, parsed.path, self.file)
            ZipFile(self.file).extractall(self.folder)
            print(exists(self.folder))
            print(exists(listdir(self.folder)[0]))
            chdir("{}/{}".format(self.folder, listdir(self.folder)[0]))
            for files in listdir():
                if path.isdir(files):
                    with suppress(FileNotFoundError):
                        rmtree("{}/{}".format(self.this, files))
                    copytree(files, "{}/{}".format(self.this, files))
                else:
                    with suppress(FileNotFoundError):
                        remove("{}/{}".format(self.this, files))
                    copyfile(files, "{}/{}".format(self.this, files))
            rmtree("../../../temp")
            exit("Run Script Again!")
            return
        print("Script is up to date!")
