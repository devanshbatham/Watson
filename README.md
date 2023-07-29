# Watson: A Note Taking CLI utility

Watson is a Python script that allows you to manage and search notes from the command line. The script uses SQLite to store note data, and provides a simple interface to add, view, delete, and search notes.

## Requirements

- Python 3.x
- `argparse` module
- `sqlite3` module
- `rich` module


## Installation

```bash
git clone https://github.com/devanshbatham/watson
cd watson
sudo chmod +x setup.sh
./setup.sh
```


## Usage

```bash
watson [subcommand] [options]
```

### Subcommands

Watson has the following subcommands:

- `init`: create the notes table in the database
- `add`: add a new note to the database
- `view`: view all notes in the database
- `delete`: delete notes from the database
- `search`: search notes in the database for a keyword


Each subcommand has its own set of options and arguments. You can view the available options and arguments for each subcommand by running:


```bash
watson [subcommand] --help
```

### Examples

Here are some examples of how to use Watson:

#### Initializing the Database

```bash
watson init
```

#### Adding a Note

To add a new note to the database, run:


```bash
watson add "This is a new note" -t "tag1, tag2"
```


This will add a new note with the text "This is a new note" and the tags "tag1" and "tag2".


#### Viewing Notes

To view all notes in the database, run:


```bash
watson view
```

This will display a table with all notes and their associated tags.


#### Deleting Notes

To delete notes from the database, run:


```bash
watson delete [options]
```

You can delete all notes, notes with a specific tag, or a note with a specific ID. For example, to delete all notes with the tag "tag1", run:


```bash
watson delete -t "tag1"
```


To delete all notes, run:

```bash
watson delete -a
```

To delete note with specified ID, run:

```
watson delete -i 3
```

#### Searching Notes

To search notes in the database for a keyword, run:


```bash
watson search "keyword"
```

This will display a table with all notes that contain the keyword in their text or tags.