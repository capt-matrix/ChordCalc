# 🎸 Guitar Chord Calculator

*"Because learning guitar chords shouldn't be harder than rocket science... but it definitely feels like it sometimes!"*

A Python program that generates guitar chord diagrams with intelligent fingering patterns and capo support. Built with love, coffee, and way too many late nights debugging why C major looked like abstract art.

## 🎯 Author

**Captain Matrix** *(aka the guy who spent 3 months perfecting a C major chord)*

*"If debugging is the process of removing software bugs, then programming must be the process of putting them in." - Edsger Dijkstra (probably about my first version)*

## 🚀 Features

- **Smart Chord Generation**
- **Ergonomic Fingering** *(Not that one)*
- **Capo Support**
- **Visual Chord Diagrams**

### Requirements
- Python 3.6+ *(Because we're not animals)*
- Fingers *(at least 3, preferably attached to hands)*
- A sense of humor *(optional but recommended)*


## 🎵 Usage

```bash
python calculator.py
```

*Pro tip: The program won't judge you for playing Wonderwall. We've all been there.*

### Chord Notation Examples

```
C          # C major (the first chord everyone learns and immediately forgets how to play clean)
Am         # A minor (the sad cousin of A major)
F#°        # F# diminished (sounds as scary as it looks)
C#m        # C# minor (for when you want to sound sophisticated)
```

*Note: I've used sharps instead of flats throughout this program because I hate flat earthers. Don't @ me. But seriously, C# = Db, D# = Eb, etc. - sharps go up in pitch (♯), flats go down (♭), but they're the same notes. It's like calling elevator music "vertical transportation ambiance" - different name, same thing.*

### Capo Usage *(The Magical Pitch Shifter)*

Add a space and fret number for capo magic:

```
C 4        # C major shape with capo on 4th fret (sounds like E major but easier to play!)
Am 2       # A minor shape with capo on 2nd fret (instant mood enhancement)
G° 7       # G diminished with capo way up there (good luck reaching that)
```

*Fun fact: Capos are like training wheels for guitarists, but cooler and more socially acceptable.*

## 📊 The Science Behind the Magic

### 🧮 Modular Arithmetic (or "Why Math Actually Rocks")

Ever wondered why there are only 12 notes but infinite possibilities? Welcome to **modular arithmetic mod 12**! 

Think of it like a clock:
- 13 o'clock? Nope, that's 1 o'clock (13 % 12 = 1)
- C + 13 semitones? That's just C# (0 + 13) % 12 = 1

This is why going up 12 frets gives you the same note an octave higher.

*Fun physics fact: Going up 1 fret multiplies the base frequency by 2^(1/12) ≈ 1.059. It's like compound interest, but for sound waves!*

### 🎼 The Sacred Triad Formulas

*"In the beginning, there was the root note. And it was good. Then came the thirds and fifths, and chaos ensued."*

- **Major (X)**: `X, X+4, X+7` *(Happy sounds for happy people)*
  - Why? Major 3rd (4 semitones) + Perfect 5th (7 semitones) = Musical sunshine ☀️
  
- **Minor (Xm)**: `X, X+3, X+7` *(Sad but beautiful)*
  - That minor 3rd (3 semitones) is what makes you want to write poetry about rain
  
- **Diminished (X°)**: `X, X+3, X+6` *(Spooky scary skeletons)*
  - Diminished 5th (6 semitones) = instant horror movie soundtrack

### 🎸 The Fret Matrix Mystery

Our guitar strings in semitones from C:
```python
strings = [4, 9, 2, 7, 11, 4]  # E-A-D-G-B-E
```

*"Why these numbers?"* you ask. Because:
- E is 4 semitones from C
- A is 9 semitones from C (or -3, but we're positive people here)
- D is 2 semitones from C
- G is 7 semitones from C
- B is 11 semitones from C *(quirky little rebel)*
- High E is 4 semitones from C *(same as low E, just an octave higher)*

*Fun tuning fact: Guitar tuning mostly follows the circle of fifths, but the B and high E strings are shifted 1 fret higher to make chord shapes more playable. Because guitarists are practical people who don't have time for perfect mathematical consistency!*

**The Circle of Fifths**:
```
C → G → D → A → E → B → F# → C# → G# → D# → A# → F → (back to C)
```
*It's like a musical merry-go-round that never stops!*

**Base frequencies of open strings** *(for the physics nerds)*:
- **Low E (6th)**: 82.41 Hz 
- **A (5th)**: 110.00 Hz 
- **D (4th)**: 146.83 Hz 
- **G (3rd)**: 196.00 Hz 
- **B (2nd)**: 246.94 Hz 
- **High E (1st)**: 329.63 Hz 

It's like a secret code that unlocks the fretboard! 🗝️

## 🎭 Easter Eggs & Fun Facts

### 🥚 Hidden Features
- Try entering "Wonderwall" *(just kidding, please don't)*
- The program secretly judges you for using more than 3 fingers
- Every time you play a diminished chord, a music theory teacher gets their wings

### 🤓 Algorithm Considerations
- **Max 3-fret stretch**: Ensures comfortable finger positioning for most hand sizes
- **No gaps rule**: Prevents muted strings in the middle of played strings (ergonomically impossible)
- **Each note max twice**: Limits chord tone repetition to avoid muddy sound and

## 🎪 Chord Diagram Decoder Ring

```
C Major [0]    ← "This is what chord, in what capo position"

 0             ← "Base fret"
 | C E G       ← "Triads (the good notes)"
x|========== X ← "x = muted (shhh, don't play this)"
3|---------- C ← "3rd fret on A plays a C"
2|---------- E ← "2nd fret on D plays an E"
0|---------- G ← "Open string on G plays G (free notes are best notes)"
1|---------- C ← "1st fret on B plays another C (redundancy for richness)"
0|---------- E ← "Open high E (the string that always goes out of tune)"
 | C          ← "Short name (for when you're feeling lazy)"
 |            ← "End of diagram (applause appreciated)"
```

## 🔍 The Algorithm Explained *(For Fellow Code Nerds)*

### Step 1: String Analysis (Top to Bottom)
*"We start from the thinnest string because it's the least intimidating"*

1. Check if open string has a chord tone → Use it! (Free notes = happy programmer)
2. Try frets 1-4 if needed → But only if we have fingers left
3. Give up and mute → Sometimes surrender is the best option

### Step 2: Ergonomic Reality Check
*"Making sure humans can actually play this thing"*

- No gaps in the middle (your hand isn't a spider)
- If A string can't contribute → Mute it AND the low E (package deal)
- Max 3 fingers (we're not octopi)

### Step 3: Pretty Printing
*"Making ASCII art that doesn't look like modern art"*

## 🛠️ Technical Specs

### Note Mapping *(The Rosetta Stone)*
```python
notes = {
    0: 'C',   # The starting point of all musical confusion
    1: 'C#',  # C but sharper (literally)
    2: 'D',   # The reliable middle child
    # ... and so on until we get back to C
}
```

## 🎨 Examples That Actually Work

### Basic Chord *(The "Hello World" of Guitar)*
```
Enter chord: C
C Major [0]
 0
 | C E G
x|========== X  ← "Low E taking a nap"
3|---------- C  ← "A string working hard"
2|---------- E  ← "D string pulling its weight"
0|---------- G  ← "G string being itself"
1|---------- C  ← "B string showing off"
0|---------- E  ← "High E, the attention seeker"
 | C
 |
```

### With Capo *(The Plot Twist)*
```
Enter chord: C 5
C Major [5]
 5             ← "Capo camping at 5th fret"
 | C E G       ← "Still C E G in theory..."
x|========== X
3|---------- F ← "But sounds like F now! 🎭"
2|---------- A
0|---------- C
1|---------- F
0|---------- A
 | F          ← "Surprise! It's actually F major!"
 |
```

## 🐛 Known Issues *(AKA "Features")*

- Program may become sentient and start critiquing your playing
- Occasionally generates chords that require yoga training
- Has been known to make people actually understand music theory *(side effects may include smugness)*

## 🤝 Contributing

Want to help make this even more awesome? 

Submit issues or PRs for:
- 🎼 Additional chord types (7ths, 9ths, "add more confusion" chords)
- 🎯 Alternative fingering suggestions (for people with different hand sizes)
- 🧠 Improved ergonomic analysis (because comfort matters)
- 🎨 Better ASCII art (always room for improvement)

*"Code is like humor. When you have to explain it, it's bad." - Cory House*

## 🌟 Connect with the Author

- 📧 **Email**: c.mctrix@gmail.com *(for serious inquiries and chord requests)*
- 💻 **GitHub**: [@capt-matrix](https://github.com/capt-matrix) *(where the magic happens)*
- 🎨 **CodePen**: [@captain_matrix](https://codepen.io/captain_matrix) *(pretty things live here)*
- 📱 **Telegram**: [@capt_matrix](https://www.t.me/capt_matrix) *(for quick hellos)*
- 📸 **Instagram**: [@captain_matrix](https://www.instagram.com/captain_matrix/) *(mostly coffee and code)*

## 📜 License

MIT License - Feel free to use, modify, and hopefully improve upon this humble attempt at digitalizing the guitar fretboard. 

*Remember: The best chord is the one you can actually play. The second best is the one that makes you sound like you know what you're doing.*

---

*"There are only 10 types of people in this world: those who understand binary, those who don't, and those who weren't expecting a base 3 joke."*

**Happy Strumming! 🎸✨**

*P.S. - If this program helped you finally nail that F major chord, I consider my life's work
