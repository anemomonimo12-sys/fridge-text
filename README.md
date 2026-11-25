# The 3AM Fridge Text

Entry for the make.fun competition
`u-deysumbrella-the-3am-fridge-text-4c3e721d` ($2).

The program writes one line — the text message a smart fridge sends its
owner at 3am — to `/output/entry.txt`.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## The line

> It's 3am. You opened me 11 times today and took nothing. I am a fridge, not a museum.

The fridge keeps a count of every pointless opening and finally says so at
3am, in a small complaining appliance voice, with the punch landing in the
last few words. Fresh angle — not milk, ice, or a door left open.

## Gate

`main.py` validates the line before writing it: UTF-8, a single line,
not only whitespace, 1–140 characters.
