"""
lotto 647: 6 numbers, n: 49
lotto max: 7 numbers, n: 50

"""

from typing import Literal, Any
import random

generatedTickets: list[list[int]] = [];

def shallowMatchesSome(match: list[Any], array: list[list[Any]]) -> bool:
    for n in array:
        for i in range(len(n)):
            m = 0
            if i < len(match) and match[i] == n[i]:
                m += 1
            else: continue
            if m == len(n) - 1: return True;
    return False

def formatTickets(tickets: list[list[int]]):
    s = '';
    for i in range(len(tickets)):
        ticket = tickets[i];
        s += f', {ticket}' if i > 0 else f'{ticket}'

    return s;

def generateUNIQUE(lotto: Literal['1'] | Literal['2'], prefs: list[int], notUnique: bool = False) -> list[int]:
    numberBin = [i for i in range(1, 50 if lotto == '1' else 51)];

    ticket: list[int] = []

    for i in prefs:
        ticket.append(i);

    for _ in range(6 - len(prefs) if lotto == '1' else 7 - len(prefs)):
        choice = random.choice(numberBin);
        numberBin.remove(choice);
        ticket.append(choice);

    if not notUnique and shallowMatchesSome(ticket, generatedTickets):
        return generateUNIQUE(lotto, []);

    return ticket;

def serveInput():
    lotto = input("Which lotto would you like to play (pick 1 or 2)?\n1. lotto 649\n2. lotto max\n");

    if lotto not in ('1', '2'):
        print(f"option {lotto} is not a valid selection. Please try again.");
        return serveInput();

    numTickets = input("How many tickets would you like to buy?\t");

    try:
        numTickets = int(numTickets);
    except Exception:
        print(f"{numTickets} is not a valid number. Please start over");
        return serveInput();

    ticketPrefs: list[int] = input("Do you have any numbers you would want to include in your tickets? (You should input each number once, separated by a space)\t").split(' ');  # type: ignore
    
    if len(ticketPrefs) > 0 and ticketPrefs[0].strip() == '':  # type: ignore
        ticketPrefs = []

    if len(ticketPrefs) > (6 if lotto == 1 else 7):
        print("You can't have more ticket preferences than numbers in the lotto. Please start over");
        return serveInput();

    for i in range(len(ticketPrefs)):
        try:
            ticketPrefs[i] = int(ticketPrefs[i]);
        except Exception:
            print(f"{ticketPrefs[i]} is not a valid number, please start over");
            return serveInput();

    for _ in range(numTickets):
        out = generateUNIQUE(lotto, ticketPrefs, True);
        generatedTickets.append(out);

    winningTicket = generateUNIQUE(lotto, [], True);
    if shallowMatchesSome(winningTicket, generatedTickets):
        print(f"You won! The winning ticket is {formatTickets([winningTicket])}");
    else:
        print(f"You lost! The winning ticket is {formatTickets([winningTicket])}. Your tickets: {formatTickets(generatedTickets)}");

serveInput();