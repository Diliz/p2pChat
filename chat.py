#!/usr/bin/env python3
import base.clientServer
import config
import base.gui

server = base.clientServer.Server(config.port)
server.start()
base.gui.root.mainloop()
