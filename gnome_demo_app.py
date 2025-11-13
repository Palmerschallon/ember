#!/usr/bin/env python3
"""
A simple GTK app to demonstrate GNOME integration
"""
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib
import json
import websocket
import threading

class GnomeWebSocketDemo(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GNOME WebSocket Demo")
        self.set_default_size(400, 300)
        self.set_border_width(10)
        
        # Main container
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)
        
        # Title
        title = Gtk.Label()
        title.set_markup("<big><b>GNOME System Monitor</b></big>")
        vbox.pack_start(title, False, False, 0)
        
        # System info labels
        self.cpu_label = Gtk.Label("CPU: ---%")
        self.memory_label = Gtk.Label("Memory: ---%")
        self.processes_label = Gtk.Label("Processes: ---")
        self.gnome_label = Gtk.Label("GNOME: ---")
        
        for label in [self.cpu_label, self.memory_label, 
                     self.processes_label, self.gnome_label]:
            label.set_alignment(0, 0.5)
            vbox.pack_start(label, False, False, 0)
        
        # Progress bars
        self.cpu_progress = Gtk.ProgressBar()
        self.memory_progress = Gtk.ProgressBar()
        
        vbox.pack_start(Gtk.Label("CPU Usage:"), False, False, 0)
        vbox.pack_start(self.cpu_progress, False, False, 0)
        vbox.pack_start(Gtk.Label("Memory Usage:"), False, False, 0)
        vbox.pack_start(self.memory_progress, False, False, 0)
        
        # Buttons
        button_box = Gtk.Box(spacing=6)
        vbox.pack_start(button_box, False, False, 0)
        
        self.connect_button = Gtk.Button(label="Connect to WebSocket")
        self.connect_button.connect("clicked", self.on_connect_clicked)
        button_box.pack_start(self.connect_button, True, True, 0)
        
        # Status
        self.status_label = Gtk.Label("Not connected")
        vbox.pack_start(self.status_label, False, False, 0)
        
        self.ws = None
        self.ws_thread = None
        
    def on_connect_clicked(self, widget):
        """Connect to the WebSocket server"""
        if self.ws is None:
            self.ws_thread = threading.Thread(target=self.websocket_client)
            self.ws_thread.daemon = True
            self.ws_thread.start()
            self.connect_button.set_label("Disconnect")
            self.status_label.set_text("Connecting...")
        else:
            if self.ws:
                self.ws.close()
            self.ws = None
            self.connect_button.set_label("Connect to WebSocket")
            self.status_label.set_text("Disconnected")
    
    def websocket_client(self):
        """WebSocket client thread"""
        try:
            self.ws = websocket.WebSocketApp("ws://localhost:8765",
                                           on_message=self.on_message,
                                           on_error=self.on_error,
                                           on_close=self.on_close,
                                           on_open=self.on_open)
            self.ws.run_forever()
        except Exception as e:
            GLib.idle_add(self.status_label.set_text, f"Error: {str(e)}")
    
    def on_message(self, ws, message):
        """Handle incoming WebSocket messages"""
        try:
            data = json.loads(message)
            GLib.idle_add(self.update_ui, data)
        except json.JSONDecodeError:
            pass
    
    def on_error(self, ws, error):
        GLib.idle_add(self.status_label.set_text, f"Error: {str(error)}")
    
    def on_close(self, ws):
        GLib.idle_add(self.status_label.set_text, "Connection closed")
        self.ws = None
        GLib.idle_add(self.connect_button.set_label, "Connect to WebSocket")
    
    def on_open(self, ws):
        GLib.idle_add(self.status_label.set_text, "Connected!")
    
    def update_ui(self, data):
        """Update UI with system stats"""
        cpu = data.get('cpu_percent', 0)
        memory = data.get('memory', {})
        processes = data.get('processes', 0)
        gnome_info = data.get('gnome', {})
        
        self.cpu_label.set_text(f"CPU: {cpu:.1f}%")
        self.cpu_progress.set_fraction(cpu / 100.0)
        
        if memory:
            mem_percent = memory.get('percent', 0)
            self.memory_label.set_text(f"Memory: {mem_percent:.1f}%")
            self.memory_progress.set_fraction(mem_percent / 100.0)
        
        self.processes_label.set_text(f"Processes: {processes}")
        
        gnome_version = gnome_info.get('gnome_version', 'Unknown')
        self.gnome_label.set_text(f"GNOME: {gnome_version}")

win = GnomeWebSocketDemo()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()