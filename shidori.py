#!/usr/bin/python3.11

import socket
import ssl
import tkinter


class URL:
    def __init__(self, url):
        self.user_agent = "Shidori-Browser/1.0"
        self.scheme, url = url.split('://', 1)
        assert self.scheme in ['http', 'https', 'file']
        if "/" not in url:
            url = url + "/"
        self.host, url = url.split("/", 1)
        self.path = "/" + url
        if self.scheme == "http":
            self.port = 80
        elif self.scheme == "https":
            self.port = 443
        if ":" in self.host:
            self.host, port = self.host.split(":", 1)
            self.port = int(port)
        


    def request(self):
        if self.scheme == "file":
            with open(self.path, "r") as f:
                body = f.read()
                
        if self.scheme in ["http", "https"]:
            s = socket.socket(
                family=socket.AF_INET,
                type=socket.SOCK_STREAM,
                proto=socket.IPPROTO_TCP,
            )
            s.connect((self.host, self.port))
            if self.scheme == "https":
                ctx = ssl._create_unverified_context()
                s = ctx.wrap_socket(s, server_hostname=self.host)
            

            s.send(("GET {} HTTP/1.1\r\n".format(self.path) +
                    "Host: {}\r\n".format(self.host) +
                    "Connection: {}\r\n".format("close") +
                    "User-Agent: {}\r\n\r\n".format(self.user_agent))
                .encode("utf8"))

            response = s.makefile("r", encoding=("utf8"), newline="\r\n")
            statusline = response.readline()
            version, status, explanation = statusline.split(" ", 2)
            response_headers = {}

            while True:
                line = response.readline()
                if line == "\r\n":
                    break
                header, value = line.split(":", 1)
                response_headers[header.casefold()] = value.strip()

            assert "transfer-encoding" not in response_headers
            assert "content-encoding" not in response_headers
            body = response.read()
            s.close()
        return body
    
def lex(body):
    text = ""
    in_tag = False
    for c in body:
        if c == "<":
            in_tag = True
        elif c == ">":
            in_tag = False
        elif not in_tag:
            text += c
    return text

WIDTH, HEIGHT = 800, 600
HSTEP, VSTEP = 13,18
SCROLL_STEP = 100


def layout(text):
        display_list = []
        cursor_x, cursor_y = HSTEP, VSTEP   
        for c in text:
            display_list.append((cursor_x, cursor_y,c))
            cursor_x += HSTEP
            if cursor_x >= WIDTH - HSTEP:
                cursor_y += VSTEP
                cursor_x = HSTEP
        return display_list


class Browser:
    def __init__(self):
        self.window = tkinter.Tk()
        self.canvas = tkinter.Canvas(
            self.window,
            width=WIDTH,
            height=HEIGHT
        )
        self.canvas.pack()
        self.scroll = 0
        self.window.bind("<Down>", self.scrolldown)
        self.window.bind("<Up>", self.scrollup)


    def load(self, url):
        body = url.request()
        text = lex(body)
        self.display_list = layout(text)
        self.draw()

    def draw(self):
        self.canvas.delete("all")
        for x,y,c in self.display_list:
            if y > self.scroll + HEIGHT: continue
            if y + VSTEP < self.scroll: continue
            self.canvas.create_text(x,y-self.scroll,text=c)

    def scrolldown(self, e):
        self.scroll += SCROLL_STEP
        self.draw()
    
    def scrollup(self, e):
        self.scroll -= SCROLL_STEP
        self.draw()


if __name__ == "__main__":
    import sys
    Browser().load(URL("https://browser.engineering/examples/xiyouji.html"))
    tkinter.mainloop()
