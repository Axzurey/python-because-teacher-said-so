"""
Super Notepad!

Creator: Michael Gharoro
Reason behind creation: The teacher made me to it 😭

"""

from typing import Literal, Union, TypedDict, Callable

class Note:
    header: str;
    body: str;

    def __init__(self, header: str, body: str):
        self.header = header;
        self.body = body;

class HeadedNotepad:
    notes: list[Note];

    def __init__(self):
        self.notes = [];

    def addNote(self, header: str, body: str) -> tuple[Literal[0] | Literal[-1], Note]:
        note = Note(header, body);
        self.notes.append(note);
        return (0, note);

    def removeNote(self, index: int) -> Note:
        return self.notes.pop(index);

    def getNoteCount(self) -> int:
        return len(self.notes);
    
    def getPrettyNote(self, index: int) -> Union[bool, str]:
        if index < 0 or index >= self.getNoteCount(): return False;

        note = self.notes[index];

        text = f"""{note.header}
-------------------------------------------------------
{note.body}
"""
        return text;

    def modifyNote(self, index: int, newHeader: Union[str, None], newBody: Union[str, None] = None) -> Union[bool, Note]:
        if index < 0 or index >= self.getNoteCount(): return False;

        self.notes[index].body = newBody if newBody else self.notes[index].body;
        self.notes[index].header = newHeader if newHeader else self.notes[index].header;

        return self.notes[index];

    def searchContains(self, check: str, checksBody: bool = False) -> tuple[Literal[0] | Literal[-1], list[tuple[Note, int]]]:
        """
        Searches for all occurences of "check" in the notes, with an optional parameter to check the body
        The output is a list of tuples(Note, Index)
        """
        notes: list[tuple[Note, int]] = [];

        i = 0;

        for note in self.notes:
            if check in note.header:
                notes.append((note, i));
            if checksBody and check in note.body:
                notes.append((note, i));

            i += 1;

        return (0, notes);

    def getNoteHeaders(self, n: int = -1) -> tuple[Literal[0] | Literal[-1], list[tuple[str, int]] | str]:
        """
        Gets the first n note headers (defaults to -1, which is all the notes) in the format: (Header, Index)
        """
        if n == -1:
            return (0, [(self.notes[i].header, i) for i in range(self.getNoteCount())]);
        else:
            return (0, [(self.notes[i].header, i) for i in range(n)]);

    def listNoteHeaders(self, n: int = -1) -> tuple[Literal[0] | Literal[-1], list[tuple[str, int]] | str]:
        [res, headers] = self.getNoteHeaders(n);

        h = 'Notes:\n';

        h += '\n'.join([f'{headers[i][1]}. {headers[i][0]}' for i in range(len(headers))]);

        return (res, h);

currentNotePad = HeadedNotepad();

class cmdInfo(TypedDict):
    alias: list[str];
    args: list[str];
    callback: Callable;
    description: str;

def getCmd(cmd: str | None) -> tuple[str, cmdInfo] | tuple[None, None]:
    if not cmd: return (None, None);

    for k in cmds.keys():
        if cmd in cmds[k]['alias']:
            cmd = k;
            break;
    
    if cmd in cmds: return (cmd, cmds[cmd]); #type: ignore

    return (None, None);

def getHelpInformation(cmd: str | None):
    if not cmd:
        st = '---Help Panel---\n\n==Commands==:\n';

        for k in cmds.keys():
            st += f"Command: {k}. Description: {cmds[k]['description']}\n";

        return st;

    cmd = cmd.strip();

    for k in cmds.keys():
        if cmd in cmds[k]['alias']:
            cmd = k;
            break;

    if cmd in cmds:
        st = f"""---Help Panel---
Command: {cmd}
Aliases: {', '.join(cmds[cmd]['alias'])}
Stages: {len(cmds[cmd]['args'])}
Description: {cmds[cmd]['description']}
""";
        return st;
    return f'{cmd} is an invalid help command. Please try again with something else.'

cmds = {
    "delete": {
        "alias": ['d', 'del'],
        "args": ['What entry index would you like to delete?\t'],
        "callback": lambda i: currentNotePad.removeNote(i),
        "description": 'Delete a note entry using it\'s index'
    },
    "find": {
        "alias": ['f', 'search'],
        "args": ['What are you searching for?\t'],
        "callback": lambda s: currentNotePad.searchContains(s, True),
        "description": 'Find all notes containing text'
    },
    "add": {
        "alias": ['a', 'new', 'create'],
        "args": ['Please input your title.\t', 'Say something~\t'],
        "callback": lambda h, b: currentNotePad.addNote(h, b),
        "description": 'Creates a new note'
    },
    "edit": {
        "alias": ['e', 'modify', 'change'],
        "args": [
            'Please enter your changes to the title. (If you plan on making no changes, you can leave it empty)\t',
            'Please enter your changes to the text. (If you plan on making no changes, you can leave it empty)\t'
        ],
        "callback": lambda i, nH, nB: currentNotePad.modifyNote(i, nH, nB),
        "description": 'Modifies the note with the provided index, with a new header or body'
    },
    "list": {
        "alias": ['l'],
        "args": ["How many notes do you want to be displayed? (If you don't care, you can leave this empty and we will show all of them)\t"],
        "callback": lambda n: currentNotePad.listNoteHeaders(n or -1),
        "description": 'Lists all the notes in the notepad'
    },
    "read": {
        "alias": ['r', 'view', 'open'],
        "args": ['Which note do you want to read? Please input the index.\t'],
        "callback": lambda i: currentNotePad.getPrettyNote(i),
        "description": 'Reads a note at the provided index'
    },
}

def acquireAndParseInput():
    msg = input('What would you like to do? (enter "help" for more information)\t').strip().lower();

    if 'help' in msg:
        helpInfo = getHelpInformation(msg.split('help')[1] or msg.split('help')[0]);

        if not helpInfo: return acquireAndParseInput();

        print(helpInfo);

        return acquireAndParseInput();
    else:
        [cmd, tbl] = getCmd(msg);

        if not cmd or not tbl:
            print(f'{msg} is an invalid command');
            return acquireAndParseInput();

        args = [];

        for i in tbl['args']:
            arg = input(i).strip();

            args.append(arg);

        [result, msg] = tbl['callback'](*args);
        
        if result == -1:
            print(f'Performing function "{cmd}" failed because "{msg}"');
            return acquireAndParseInput();
        else:
            if msg: print(msg);
            print('Operation successful; Please continue.');
            return acquireAndParseInput();

def start_main_loop():
    while True:
        acquireAndParseInput();



start_main_loop();