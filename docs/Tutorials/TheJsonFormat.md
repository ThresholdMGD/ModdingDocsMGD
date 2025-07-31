---
search:
  boost: 0.8
---

# The JSON Format
**While this page is optional towards the process of getting familiar
with modding,** knowing the format you're editing in is vastly helpful
in comprehension and understanding of what you're doing. Later pages in
the documentation for example will presume you know the difference
between a json key, and a json value.

This page will cover an exercise of the JSON file format, and get you
generally familiar with your editor, and terminology of JSON. Make a new
file with the file type ".json" at the end in your editor of choice.
You will be creating a basic
[Event](../Manual/Events/Events.md).

!!! info "See also"

    For editors that report improper JSON formatting in real-time, see
[Pulsar or VS Code](../GettingStarted/Editors.md) feature list. Especially VS Code for its tailored MGD
Extension that verifies you're building a structure correctly.

## Object
Start by making a set of curly brackets with an empty line between them,
like the below. You may notice that your editor automatically makes a
set of curly brackets.

``` json
{

}
```

This is called an **object**. Any JSON data you encounter will be within
an object. You can have objects inside other objects, as many .json
files for MGD will utilize.

The brackets can be on the same line, as JSON does not care about
[whitespace](https://www.computerhope.com/jargon/w/whitspac.htm).
However, keeping them on separate lines improves readability for anyone
reading it later, including yourself.

## Keys & Strings
Objects can't contain data directly. That's the job of **keys**. Put
this text in the empty line between the brackets:

``` json
"name": "",
```

Anything typed within double quotes (such as `"name"` or `""` in the
above) is what is called a **string**. You can put anything inside a
string.

Any string followed by a colon `:` is a key, such as `"name":` in the
above. Keys are always made out of strings. You provide keys with values
after the colon. In the case of MGD, those values will always be
strings. You will not be making custom keys yourself, you will be using
existing keys made by Threshold, depending on what you're making.
# Note that whitespace is important when inside of a string.
Lastly, **ensure it ends with a comma**. Without it, it will not know it
needs to move onto the next key. As a reminder, do be sure to use a
Linter for real-time error warnings.

If you haven't already, provide the `"name":` key's string with some
text characters for now, such as `"Test Event"`

## String Expectations
Start a new line after the name key while keeping it inside the object,
and copy/paste the following\...

``` json
"CardType": "Event",
"CardLimit": "1",
"Description": "A description",
```

You can become familiar with what these keys do in
[Event Creation](../Manual/Events/Events.md) later.

Sometimes, keys are designed to expect specific string values, such as
`"CardType":` expecting a certain type of event card type, in this case,
a plain `"Event"` card type. `"CardLimit":` is expecting numerical
values inside of its string. `"Description":`, much like `"name":`, can
be provided with anything inside the string that the user wishes.

## Arrays
``` json
"requires": ["Anaph Herb", "Vandal Note"],
```

`"requires":` is given an a set of square brackets `[]`. This is called
an **Array**. Arrays allow any number of values to be provided in the
scenario a key is meant to be provided with more than one value. As
expected, these values are strings.

Note, each string you provide within the array must still be separated
from one another with a comma. The last string marks the end of the
array, and thus has no comma so it knows to exit the array.

Arrays cannot contain keys, only objects can. However,
*arrays* can contain objects.

## Nested Objects
``` json
"Speakers": [
{
  "name": "Perpetua",
  "postName": "",
  "SpeakerType": ""
},
{
  "name": "Elena",
  "postName": "",
  "SpeakerType": ""
}
],
```

Here, the `"Speakers":` key is given an array, but instead of giving the
array a series of strings, it's given a series of objects. As said
earlier, you can have objects within objects, which is done by providing
a key with an array containing objects.

As a reminder, objects, unlike arrays, can't contain values directly,
but can contain keys with values. Which could also have arrays, then
more objects, and so forth. This act is called **nesting**.

For the `"Speakers":` array of objects, it expects the three keys with
their string values above in each object. The last two in this case, can
be provided with blank strings. Note the comma between the objects, and
how the last object doesn't have one, so it can leave the array and
move onto the next key.

## Conclusion
``` json
"EventText": [
    {
    "NameOfScene": "EventStart",
    "theScene": [
        "DisplayCharacters",
        "1",
        "2",
        "EndLoop",
        "Speaks2",
        "You will handle all my paperwork from here on!",
        "ChangeImageLayer", "Expression", "1", "Panic",
        "Speaks",
        "{b}Noooo{/b}, anything but {i}paperwork{/i}!"
        ]
    }
  ]
```

Here is the final top-level key the Event json expects. Note that the
square bracket on the final line of the code block isn't followed by a
comma, as this is final key, marking the end of the parent object, the
end of the json file, and this overview of the JSON format.

!!! info "See also"

    If you want a better grasp at how JSON works in general outside of the
context of MGD, see
[here](https://www.w3schools.com/js/js_json_syntax.asp).

For an advanced technical explanation, see
[here](https://www.json.org/json-en.html).
