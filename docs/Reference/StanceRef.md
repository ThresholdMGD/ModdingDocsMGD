# Stance Reference

!!! info "See also"

    See Stances for information on functions
    related to stances, and Stance Restraints for information on lineTriggers related to specific stances.


## Any, None

`"Any"`, or `"None"` can sometimes be checked for in certain cases to
either cover any stance, or the lack of any stance. The documentation
for relevant functions and *keys* will
state whether these *values* are an
option.

## Player & Monster Stances

The following three stances can be initiated by both players and most
monsters:

-   `"Sex"`
-   `"Anal"`
-   `"Making Out"`
-   `"Penetration"`

Penetration is an internal stance type that counts both Sex and Anal,
for use in [Skills](../Manual/Skills/Skills.md) when checking for usability. **It cannot be used for
starting stances in functions, nor as a parameter for Loss/Victory
scenes.**

## Monster Stances

The following stances can only be started by monster girls, and are
meant to count towards particular fetishes:

-   `"Blowjob"`
-   `"Titfuck"`
-   `"Tailjob"`
-   `"Tail Fuck"` (e.g. Tail Pussy)
-   `"Tail Pegging"`
-   `"Face Sit"`
-   `"Footjob"`
-   `"Breast Smother"`
-   `"Nursing"`
-   `"Thighjob"`
-   `"Thigh Grinding"`

## Specialty Stances

The following stances can only be started by monster girls, and are
specialized with no particular fetishes.

-   `"Cuddle"`
-   `"Slimed"`
-   `"Slimed 50%"`
-   `"Slimed 100%"`

## Making Stances

Stances are completely nebulous. Anything can be a stance, and thus can
be declared freely, there doesn't need to be any particular point of
origin, nor followed rules. Thus, it can be safely checked for or
declared at any point in a function or key, even if it doesn't actually
exist anywhere else yet. Just remember they're case sensitive.

Note that player skills and other stances may require
Skill Additions in order to be made
fully aware of the custom stances in scenarios where it might not make
sense for a certain set of skills or stances to be available. For
example, no Making Out or Kiss during a Head-Standing stance.
