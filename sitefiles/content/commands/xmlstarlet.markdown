xmlstarlet 

xmlstarlet [options...] {command} [cmd-options...]

Most often run as a two word command: xmlstarlet [command]

Things I've done:

 - Un-escaped output
 - Pretty-printed
 - Validated xml
 - Output values matching a string (catalog number, lot number)
 - Output all instances of an element (ID number, etc.)

Most common commands I've used:

xmlstarlet sel

 - Probably the one you'll use most frequently
 - Remember the namespaces!!!

options 

-N (for namespaces)

 - you need this if your xml uses declared namespaces
 - 


xmlstarlet el

see options with 

xmlstarlet el --help

    - prints just the element structure
    - useful for getting an overview of the xml for further querying
    - can only use one option at a time

Man page is mostly a pointer to --help messages


Need to review:

 - XML terminology
 - XSL
