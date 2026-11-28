#!/bin/bash

# 1. Accept input text
INPUT_TEXT="$1"

if [ -z "$INPUT_TEXT" ]; then
    echo "Usage: $0 \"Japanese text here\""
    exit 1
fi

# 2. Parse text into unique dictionary forms using MeCab
# %f[6] extracts the base lemma/dictionary form of a word
WORDS=$(echo "$INPUT_TEXT" | mecab -F"%f[6]\n" -E"" | grep -v '^\*' | sort -u)

# 3. Loop through words, convert reading to Hiragana, and fetch definitions
for WORD in $WORDS; do
    echo "====================================="
    echo "🇯🇵 Word: $WORD"
    
    # Extract Hiragana Reading via MeCab and Perl
    HIRAGANA=$(echo "$WORD" | mecab -F"%f[7]\n" -E"" | grep -v '^\*' | perl -Mutf8 -C -pe 'tr/ァ-ン/ぁ-ん/')
    echo "💬 Reading: $HIRAGANA"
    
    # Query Jisho API using curl and parse the top definition using standard grep/sed
    echo -n "📖 Meaning: "
    curl -s "https://jisho.org" | \
        grep -o '"english_definitions":\[[^]]*\]' | head -n 1 | \
        sed 's/"english_definitions":\[//g; s/\]//g; s/"//g'
done
echo "====================================="

