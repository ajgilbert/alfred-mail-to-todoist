#!/usr/bin/osascript  -l JavaScript -s o

var app = Application('Mail')

messages = app.selection()

for (let i = 0; i < messages.length; i++) {
    messages[i].flagIndex = -1
    messages[i].backgroundColor = "none"
}
