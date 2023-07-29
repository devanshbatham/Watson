#!/usr/bin/env python3

"""Watson: A note taking CLI"""

import argparse
import sqlite3
import re
from rich.console import Console
from rich.table import Table


def init(args):
    """Create a notes table in the database"""
    conn = sqlite3.connect("/root/notes.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS notes
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 note TEXT,
                 tags TEXT)''')
    conn.commit()
    conn.close()
    print(" 🎉 Notes table created successfully")


def add_note(args):
    """Add a new note to the database"""
    conn = sqlite3.connect("/root/notes.db")
    c = conn.cursor()
    note = args.note
    tags = args.tags
    if tags:
        tags = tags.split(",")
        tags = [tag.strip() for tag in tags]
        tags_str = ",".join(tags)
    else:
        tags_str = None
    c.execute("INSERT INTO notes (note, tags) VALUES (?, ?)", (note, tags_str))
    conn.commit()
    print(" 🎉 Note added successfully")
    if args.show:
        view_notes(args)
    conn.close()


def view_notes(args):
    """View all notes in the database"""
    conn = sqlite3.connect("/root/notes.db")
    c = conn.cursor()
    c.execute("SELECT * FROM notes")
    notes = c.fetchall()

    console = Console()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=4)
    table.add_column("Note")
    table.add_column("Tags", style="dim")

    tags = set()
    for note in notes:
        note_tags = note[2]
        if note_tags:
            note_tags = note_tags.split(",")
            note_tags = [tag.strip() for tag in note_tags]
            tags.update(note_tags)
            note_tags_str = ", ".join(note_tags)
        else:
            note_tags_str = ""

        table.add_row(str(note[0]), note[1], note_tags_str)

    console.print("\nYour notes:\n")
    console.print(table)

    console.print("\nAll tags:\n")
    for tag in tags:
        console.print(f"- {tag}")

    conn.close()


def delete_notes(args):
    """Delete notes from the database"""
    conn = sqlite3.connect("/root/notes.db")
    c = conn.cursor()
    if args.all:
        c.execute("DELETE FROM notes")
        conn.commit()
        print(" ❌ All notes deleted successfully")
    elif args.tag:
        tag = args.tag
        c.execute("DELETE FROM notes WHERE tags LIKE ?", (f"%{tag}%",))
        conn.commit()
        print(f" ❌ All notes with tag '{tag}' deleted successfully")
    elif args.id:
        note_id = args.id
        c.execute("DELETE FROM notes WHERE id=?", (note_id,))
        conn.commit()
        print(f" ❌ Note with ID {note_id} deleted successfully")
    conn.close()


def search_notes(args):
    """Search notes in the database for a keyword"""
    conn = sqlite3.connect("/root/notes.db")
    c = conn.cursor()
    query = args.query.lower()
    c.execute("SELECT * FROM notes")
    notes = c.fetchall()

    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=4)
    table.add_column("Note")
    table.add_column("Tags", style="dim")

    for note in notes:
        if query in note[1].lower() or (note[2] and query in note[2].lower()):
            note_tags = note[2]
            if note_tags:
                note_tags_str = ", ".join(note_tags.split(","))
            else:
                note_tags_str = ""
            table.add_row(str(note[0]), note[1], note_tags_str)

    console = Console()
    console.print(f" 🔍 Notes containing '{query}':\n")
    console.print(table)

    conn.close()


# Create the argument parser
parser = argparse.ArgumentParser(description="Note taking CLI")
subparsers = parser.add_subparsers()

# Create table subcommand
init_parser = subparsers.add_parser("init", help="Create notes table")
init_parser.set_defaults(func=init)

# Add subcommand
add_parser = subparsers.add_parser("add", help="Add a new note")
add_parser.add_argument("note", help="The note to add")
add_parser.add_argument("-t", "--tags", help="Tags for the note (optional)")
add_parser.add_argument("-s", "--show", action="store_true", help="Show all notes after adding (optional)")
add_parser.set_defaults(func=add_note)

# View subcommand
view_parser = subparsers.add_parser("view", help="View all notes")
view_parser.set_defaults(func=view_notes)

# Delete subcommand
delete_parser = subparsers.add_parser("delete", help="Delete notes")
delete_parser.add_argument("-a", "--all", action="store_true", help="Delete all notes (optional)")
delete_parser.add_argument("-t", "--tag", help="Delete all notes with this tag (optional)")
delete_parser.add_argument("-i", "--id", type=int, help="Delete note with this ID (optional)")
delete_parser.set_defaults(func=delete_notes)

# Search subcommand
search_parser = subparsers.add_parser("search", help="Search notes for a keyword")
search_parser.add_argument("query", help="Keyword to search for")
search_parser.set_defaults(func=search_notes)


# Parse the arguments and call the appropriate function
args = parser.parse_args()
if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()