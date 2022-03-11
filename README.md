# American-British-variety-classifier

A minimalistic spelling- and vocabulary-based American-vs-British variety classifier.

## Description

This classifier is based on the [VarCon database](http://wordlist.aspell.net/varcon/). First the database was read and used in its entirety, after which progressive prunings were performed to improve performance.

The classifier performs rudimentary preprocessing (some weird character deletion to reduce the odds of discarding non-important words) and then checks all lowercase nonnumerical words if they are present in the dictionary. The final step is assigning variety to the input text, for which we use the following logic:
* for documents with no identified American or British lexemes we return `UNK`, 
* if one variant has more than twice as many identified words as the other, we classify the instance as the more frequent variant,
* else we classify it as `MIX`.


## Files

Only two files are needed for this tool:
* `lexicon.pickle`: pickled python dictionary with words and their variants,
* `ABClf.py`: main and helper functions for preprocessing and classifying.

Later a new file was added, `lexicon_balanced.pickle`. Balanced lexicon contains about the same amount of British and American (US) keywords, which can be more fair in some cases.

## Use


Please refer to [`demo.ipynb`](demo.ipynb).

## Copyright of the original VarCon database

```
Copyright 2000-2020 by Kevin Atkinson (kevina@gnu.org) and Benjamin
Titze (btitze@protonmail.ch).

Copyright 2000-2019 by Kevin Atkinson

Permission to use, copy, modify, distribute and sell this array, the
associated software, and its documentation for any purpose is hereby
granted without fee, provided that the above copyright notice appears
in all copies and that both that copyright notice and this permission
notice appear in supporting documentation. Kevin Atkinson makes no
representations about the suitability of this array for any
purpose. It is provided "as is" without express or implied warranty.

Copyright 2016 by Benjamin Titze

Permission to use, copy, modify, distribute and sell this array, the
associated software, and its documentation for any purpose is hereby
granted without fee, provided that the above copyright notice appears
in all copies and that both that copyright notice and this permission
notice appear in supporting documentation. Benjamin Titze makes no
representations about the suitability of this array for any
purpose. It is provided "as is" without express or implied warranty.

Since the original words lists come from the Ispell distribution:

Copyright 1993, Geoff Kuenning, Granada Hills, CA
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions
are met:

1. Redistributions of source code must retain the above copyright
   notice, this list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright
   notice, this list of conditions and the following disclaimer in the
   documentation and/or other materials provided with the distribution.
3. All modifications to the source code must be clearly marked as
   such.  Binary redistributions based on modified source code
   must be clearly marked as modified versions in the documentation
   and/or other materials provided with the distribution.
(clause 4 removed with permission from Geoff Kuenning)
5. The name of Geoff Kuenning may not be used to endorse or promote
   products derived from this software without specific prior
   written permission.

THIS SOFTWARE IS PROVIDED BY GEOFF KUENNING AND CONTRIBUTORS ``AS IS'' AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED.  IN NO EVENT SHALL GEOFF KUENNING OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
SUCH DAMAGE.

```