<h1 align="center">
    Watson
  <br>
</h1>

<h4 align="center">Watson is a utility for note management and search from your terminal</h4>


<p align="center">
  <a href="#requirements">📋 Requirements</a>
  <a href="#installation">🏗️ Installation</a>
  <a href="#usage">⛏️ Usage</a>
  <br>
</p>


# Requirements

- Python 3.x
- `argparse` module
- `sqlite3` module
- `rich` module


# Installation

```sh
git clone https://github.com/devanshbatham/watson
cd watson
sudo chmod +x setup.sh
./setup.sh
```


# Usage

```sh
watson [subcommand] [options]
```

## Subcommands

<p align="center">
  <table>
    <tr>
      <th>Subcommand</th>
      <th>Description</th>
    </tr>
    <tr>
      <td><code>init</code></td>
      <td>Create the notes table in the database</td>
    </tr>
    <tr>
      <td><code>add</code></td>
      <td>Add a new note to the database</td>
    </tr>
    <tr>
      <td><code>view</code></td>
      <td>View all notes in the database</td>
    </tr>
    <tr>
      <td><code>delete</code></td>
      <td>Delete notes from the database</td>
    </tr>
    <tr>
      <td><code>search</code></td>
      <td>Search notes in the database for a keyword</td>
    </tr>
  </table>
</p>


For options and arguments of each subcommand, run:

```sh
watson [subcommand] --help
```

## Examples

### Initializing the Database

```sh
watson init
```

### Adding a Note

```sh
watson add "This is a new note" -t "tag1, tag2"
```

### Viewing Notes

```sh
watson view
```

### Deleting Notes

```sh
watson delete [options]
```

- Delete all notes with a specific tag:

```sh
watson delete -t "tag1"
```

- Delete all notes:

```sh
watson delete -a
```

- Delete note with specified ID:

```sh
watson delete -i 3
```

### Searching Notes

```sh
watson search "keyword"
```
