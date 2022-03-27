#!/usr/bin/env python3
import frida
import sys
import threading

lock = threading.Lock()
lock.acquire()
device = frida.get_usb_device()
pid = device.spawn("org.whispersystems.signal")
session = device.attach(pid)
with open("agent.js", "r", encoding="utf-8") as f:
    agent = f.read()


def on_message(message, data):
    #print("on_message:", message)
    if message['payload']['event'] == "db-opened":
        print("Database file: %s" % (message['payload']['filename']))
    if message['payload']['event'] == "found-key":
        print("Database key: %s" % (message['payload']['key']))
        session.detach()
        lock.release()


script = session.create_script(agent)
script.on("message", on_message)
script.load()
device.resume(pid)
print("Waiting for Signal to start...")
lock.acquire()
