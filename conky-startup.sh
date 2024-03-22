#!/bin/sh

# Jonas Stolt, jontas@gmx.com
# Lägg i autostart. Det väntar på att xfce är uppstartat.
# Anpassa om det skall startas med en systemd timer.

if [ "$DESKTOP_SESSION" = "xfce" ]; then 
   killall conky
   cd "$HOME/.conky/RSS-feed"
   conky -c "$HOME/.conky/RSS-feed/RSS.conf" &
   exit 0
fi
