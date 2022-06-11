#!/usr/bin/osascript  -l JavaScript -s o

var app = Application('Mail')

messages = app.selection()

messages.sort(function(a, b) {
    return b.dateSent() - a.dateSent();
});

messages[0].flagIndex = 0
messages[0].backgroundColor = "red"
