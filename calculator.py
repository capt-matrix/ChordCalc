notes = {
    0: 'C', 1: 'C#', 2: 'D', 3: 'D#', 4: 'E', 5: 'F',
    6: 'F#', 7: 'G', 8: 'G#', 9: 'A', 10: 'A#', 11: 'B'
}

thirds = {
    0: 'Maj. I', 1: 'min. ii', 2: 'min. iii', 3: 'Maj. IV',
    4: 'Maj. V', 5: 'min. vi', 6: 'dim. vii°'
}

pattern = [0, 2, 2, 1, 2, 2, 2]
strings = [4, 9, 2, 7, 11, 4]

def displayChordDiagram(chord, triad, rootind, capoFret):
    chords = chord.split()
    root = chords[0]
    chordType = chords[1] + " " + chords[2] if len(chords) > 2 else chords[1]
    
    isCapo = capoFret > 0
    
    shortNameMap = {
        'Maj. I': root,
        'min. ii': root + 'm',
        'min. iii': root + 'm', 
        'Maj. IV': root,
        'Maj. V': root,
        'min. vi': root + 'm',
        'dim. vii°': root + '°',
        'Major': root,
        'minor': root + 'm',
        'diminished': root + '°'
    }
    shortName = shortNameMap.get(chordType, root)
    
    if isCapo and capoFret > 0:
        actualRoot = (rootind + capoFret) % 12
        actualRootName = notes[actualRoot]
        actualShortName = shortName.replace(root, actualRootName)
    else:
        actualShortName = shortName
    
    print(f"\n{chord} [{capoFret}]")
    print()
    
    fretPos = ['x'] * 6
    noteCount = {note: 0 for note in triad}
    fingersUsed = 0
    
    for stringIdx in range(5, -1, -1):
        stringNote = strings[stringIdx]
        foundChordTone = False
        
        if stringNote % 12 in triad:
            note = stringNote % 12
            if noteCount[note] < 2:
                fretPos[stringIdx] = 0
                noteCount[note] += 1
                foundChordTone = True
        
        if not foundChordTone and fingersUsed < 3:
            for fret in range(1, 5):
                noteAtFret = (stringNote + fret) % 12
                if noteAtFret in triad and noteCount[noteAtFret] < 2:
                    usedFrets = [f for f in fretPos if isinstance(f, int) and f > 0]
                    if not usedFrets or abs(fret - max(usedFrets)) <= 3:
                        fretPos[stringIdx] = fret
                        noteCount[noteAtFret] += 1
                        fingersUsed += 1
                        foundChordTone = True
                        break
        
        if not foundChordTone:
            fretPos[stringIdx] = 'x'
    
    firstPlayedString = None
    for i in range(6):
        if fretPos[i] != 'x':
            firstPlayedString = i
            break
    
    if firstPlayedString is not None:
        for i in range(firstPlayedString):
            fretPos[i] = 'x'
        
        for i in range(firstPlayedString + 1, 6):
            if fretPos[i] == 'x':
                stringNote = strings[i]
                foundReplacement = False
                
                if stringNote % 12 in triad:
                    fretPos[i] = 0
                    foundReplacement = True
                elif fingersUsed < 3:
                    for fret in range(1, 5):
                        noteAtFret = (stringNote + fret) % 12
                        if noteAtFret in triad:
                            usedFrets = [f for f in fretPos if isinstance(f, int) and f > 0]
                            if not usedFrets or abs(fret - max(usedFrets)) <= 3:
                                fretPos[i] = fret
                                fingersUsed += 1
                                foundReplacement = True
                                break
                
                if not foundReplacement and i == 1:
                    fretPos[0] = 'x'
                    fretPos[1] = 'x'
                    break
                elif not foundReplacement and i == 2:
                    fretPos[0] = 'x'
                    fretPos[1] = 'x'
                    fretPos[2] = 'x'
                    break
                elif not foundReplacement:
                    fretPos[i] = 'x'
    
    if isCapo and capoFret > 0:
        baseFret = capoFret
    else:
        allFrets = [f for f in fretPos if isinstance(f, int)]
        mutedStrings = [f for f in fretPos if f == 'x']
        
        if len(mutedStrings) <= 1 and allFrets:
            baseFret = min(allFrets)
        else:
            baseFret = 0
    
    print(f" {baseFret}")
    
    triadNotes = " ".join([notes[note] for note in triad])
    print(f" | {triadNotes}")
    
    stringNames = ['E', 'A', 'D', 'G', 'B', 'E']
    for stringIdx, (stringName, fret) in enumerate(zip(stringNames, fretPos)):
        if fret == 'x':
            if stringIdx == 0:
                print(f"x|========== X")
            else:
                print(f"x|---------- X")
        else:
            fretVal = fret if isinstance(fret, int) else 0
            baseNote = (strings[stringIdx] + fretVal) % 12
            
            if isCapo and capoFret > 0:
                actualNote = (baseNote + capoFret) % 12
            else:
                actualNote = baseNote
                
            producedNote = notes[actualNote]
            if stringIdx == 0:
                print(f"{fret}|========== {producedNote}")
            else:
                print(f"{fret}|---------- {producedNote}")
    
    print(f" | {actualShortName}")
    print(" |")
    print()

def chordFromNotation(chordNotation):
    chordNotation = chordNotation.strip()
    
    if chordNotation.lower() == 'wonderwall':
        print("\n'Today is gonna be the day that they're gonna throw it back to you...'")
        print("Here's the Wonderwall progression:")
        chords = ['Em7', 'Cadd9', 'D', 'Cadd9']
        for chord in chords:
            chordFromNotation(chord)
        return
    
    if chordNotation.lower() == 'smoke on the water':
        print("\n*DUN DUN DUN, DUN DUN DA-DUN, DUN DUN DUN, DUN DA-DUN*")
        print("The most overplayed riff in guitar store history!")
        print("Frets: 0-3-5, 0-3-6-5, 0-3-5, 0-3-5-3-0")
        return
    
    if chordNotation.lower() == 'stairway':
        print("\nNO STAIRWAY TO HEAVEN!")
        print("*Wayne's World guitar store flashbacks*")
        print("But here's Am to get you started on your musical journey...")
        chordFromNotation('Am')
        return
    
    if chordNotation.lower() == 'hotel california':
        print("\n'Welcome to the Hotel California 8) ...'")
        print("Such a lovely place (such a lovely place)...")
        print("Here's the iconic Bm chord:")
        chordFromNotation('Bm')
        return
    
    if chordNotation.lower() in ['42', 'meaning of life']:
        print("\nThe Answer to Life, Universe, and Everything is... 42!")
        print("But the question was actually about guitar chords.")
        print("Here's F# major (the 42nd most annoying chord to play) XD :")
        chordFromNotation('F#')
        return
    
    if chordNotation.lower() == 'captain matrix':
        print("\nHello there! You found me! :> ")
        print("Thanks for using my chord calculator!")
        print("Here's a nice C major for you:")
        chordFromNotation('C')
        return
    
    if chordNotation.lower() in ['help', '?']:
        print("\nGUITAR CHORD CALCULATOR HELP")
        print("Format: [Note][Quality] [Capo]")
        print("Examples: C, Am, F#°, Bb, C#m")
        print("With capo: C 4, Am 2, G° 7")
        print("Easter eggs: Try 'wonderwall', 'smoke on the water', 'stairway'")
        return
    
    
    parts = chordNotation.split()
    
    capoFret = 0
    if len(parts) == 2:
        chordPart = parts[0]
        try:
            capoFret = int(parts[1])
            if capoFret > 12:
                print("Capo above 12th fret? Are you a hummingbird?")
                print("Let's bring that down to something human-playable...")
                capoFret = 12
        except ValueError:
            print(f"Error: Invalid capo fret '{parts[1]}'. Must be a number.")
            return
    else:
        chordPart = chordNotation
    
    if len(chordPart) >= 2 and chordPart[1] == '#':
        rootName = chordPart[:2]
        quality = chordPart[2:]
    elif len(chordPart) >= 2 and chordPart[1] == 'b':
        rootName = chordPart[:2]
        quality = chordPart[2:]
    else:
        rootName = chordPart[0]
        quality = chordPart[1:]
    
    root = None
    for noteNum, noteName in notes.items():
        if noteName == rootName:
            root = noteNum
            break
    
    if root is None:
        print(f"Error: Unknown root note '{rootName}'")
        print("Try: C, D, E, F, G, A, B (with optional # or b)")
        return
    
    if quality == '' or quality.upper() == 'MAJ':
        triad = [root, (root + 4) % 12, (root + 7) % 12]
        chordType = "Major"
        longName = f"{rootName} {chordType}"
        if rootName == 'F' and capoFret == 0:
            print("Ah, the dreaded F major! The chord that breaks beginners' spirits!")
    elif quality.lower() == 'm' or quality.lower() == 'min':
        triad = [root, (root + 3) % 12, (root + 7) % 12]
        chordType = "minor"
        longName = f"{rootName} {chordType}"
        if rootName == 'F' and quality.lower() == 'm':
            print("Fm is much kinder than F major. Your fingers will thank you!")
    elif quality == '°' or quality.lower() == 'dim':
        triad = [root, (root + 3) % 12, (root + 6) % 12]
        chordType = "diminished"
        longName = f"{rootName} {chordType}"
        print("Diminished chord detected! Prepare for spooky vibes...")
    else:
        print(f"Error: Unknown chord quality '{quality}'")
        print("Supported: '' (major), 'm' (minor), '°' (diminished)")
        print("Example: C, Cm, C°")
        return
    
    displayChordDiagram(longName, triad, root, capoFret)

while True:
    try:
        userInput = input("\nEnter chord: ")
        print('\n')
        if userInput.lower() in ['quit', 'exit', 'bye']:
            print("Thanks for jamming! Keep practicing!")
            break
        chordFromNotation(userInput)
    except KeyboardInterrupt:
        print("\n\nCaught you trying to Ctrl+C! Thanks for using the calculator!\n")
        break
    except Exception as e:
        print(f"Oops! Something went wrong: {e}")
        print("Try 'help' if you're stuck!")
