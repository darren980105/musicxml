from music21 import stream, note, chord, meter, key, metadata, clef
import random

def generate_piano_score(output_filename):
    # 1. 建立總譜
    score = stream.Score()
    score.metadata = metadata.Metadata()
    score.metadata.title = '古典鋼琴練習曲 - 雙手版'
    score.metadata.composer = 'Python music21'

    # 2. 建立右手聲部 (Treble Clef)
    right_hand = stream.Part()
    right_hand.append(clef.TrebleClef())
    right_hand.append(key.Key('C'))
    right_hand.append(meter.TimeSignature('4/4'))

    # 3. 建立左手聲部 (Bass Clef)
    left_hand = stream.Part()
    left_hand.append(clef.BassClef())
    left_hand.append(key.Key('C'))
    left_hand.append(meter.TimeSignature('4/4'))

    # 定義常用的 C 大調和弦進進行 (I - IV - V - I)
    # 每個和弦對應左手的音 (低八度)
    chord_progression = [
        ['C3', 'E3', 'G3'],  # C Major (I)
        ['F2', 'A2', 'C3'],  # F Major (IV)
        ['G2', 'B2', 'D3'],  # G Major (V)
        ['C3', 'E3', 'G3']   # C Major (I)
    ]

    print("正在生成雙手樂譜...")

    # 生成 4 小節 (重複兩次共 8 小節)
    for _ in range(2):
        for chords_notes in chord_progression:
            # --- 左手部分：每一小節彈奏一個大和弦 ---
            l_chord = chord.Chord(chords_notes)
            l_chord.quarterLength = 4.0  # 持續一整小節
            left_hand.append(l_chord)

            # --- 右手部分：隨機生成對應和弦音的旋律 ---
            # 為了好聽，旋律音會盡量從當前和弦的音階中選擇
            melody_pool = [p.replace('2', '4').replace('3', '5') for p in chords_notes]
            current_beat = 0
            while current_beat < 4:
                n = note.Note(random.choice(melody_pool))
                dur = random.choice([0.5, 1.0])
                n.quarterLength = dur
                right_hand.append(n)
                current_beat += dur

    # 4. 合併聲部到總譜
    score.insert(0, right_hand)
    score.insert(0, left_hand)

    # 5. 匯出 MusicXML
    score.write('musicxml', fp=output_filename)
    print(f"成功！雙手樂譜已儲存至: {output_filename}")

if __name__ == "__main__":
    generate_piano_score("piano_classical_with_left_hand.xml")