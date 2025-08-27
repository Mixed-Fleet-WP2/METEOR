parser grammar Model;

options { tokenVocab=CommonLexer; }

import Action, Part;

model
    : (action | part)* EOF
    ;