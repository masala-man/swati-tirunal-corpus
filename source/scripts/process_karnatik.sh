#!/bin/sh
# For processing text filesthat contain the complete
# text from a compositon page on karnatik.com

# Define vowel and consonant symbols
vowels="aAiIuUeEoO"
consonants="kgcjJTDNtdnylvsShLzZ"
# Remove header text
# r̥ = match and substitute /r/g between two consonants 
# ṃ = case-insensitive /m/i at the end of a word
# ā ī ū ē ō ḥ ṭ ḍ ṇ ḷ = match uppercase or double letters to their appropriate vowel/consonant symbol
# Match section delimiters and format them into valid forms
# Remove all irrelevant text
# Add the stripped pallavi header back
for file in ../texts_karnatik/*
do
	sed -i 's///g' \
	-e '1,/^pallavi$/d' \
	-e '/Meaning/,$d' \
	-e "s/\([$consonants]\)r\([$consonants]\)/\1r̥\2/g" \
	-e "s/m\b/ṃ/gi" \
	-e "s/A/ā/g" \
	-e "s/aa/ā/g" \
	-e "s/I/ī/g" \
	-e "s/ee/ī/g" \
	-e "s/U/ū/g" \
	-e "s/oo/ū/g" \
	-e "s/E/ē/g" \
	-e "s/O/ō/g" \
	-e "s/H/ḥ/g" \
	-e "s/jny/ñ/g" \
	-e "s/T/ṭ/g" \
	-e "s/D/ḍ/g" \
	-e "s/N/ṇ/g" \
	-e "s/L/ḷ/g" \
    -e "s/sh/ś/g" \
    -e "s/S/ṣ/g" \
	-e "s/anupallavi/\$ANUPALLAVI/g" \
	-e "s/caraṇaṃ [0-9]/\$CHARANAM/g" $file;
    sed -i "1 i\$PALLAVI" $file;
done
