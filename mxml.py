from music21 import stream, note, chord, meter, key, metadata, clef, articulations, tempo
import random

def add_strict_2_measure_chords(rh_part, lh_part, num_measures, chord_prog):
    """
    結構規則：
    1. 每 8 小節隨機更換一次左手旋律風格。
    2. 每個和弦固定持續 2 小節 (2+2+2+2 = 8)。
    """
    num_cycles = num_measures // 8
    
    for cycle in range(num_cycles):
        # 每 8 小節變換一次性格
        phrase_style = random.choice(['syncopated', 'running', 'lyrical'])
        
        # 遍歷 4 個和弦 (C, Am, F, G)
        for chord_notes in chord_prog:
            # 每個和弦「必須」持續 2 小節
            for m in range(2):
                # --- 左手：主旋律 ---
                curr_beat = 0
                base_pitches = [p.replace('2', '3').replace('1', '2') for p in chord_notes]
                
                while curr_beat < 4:
                    if phrase_style == 'syncopated':
                        d = random.choice([0.25, 0.5, 0.75])
                    elif phrase_style == 'running':
                        d = 0.5
                    else: # lyrical
                        d = random.choice([1.0, 2.0])
                    
                    if curr_beat + d > 4: d = 4 - curr_beat
                    
                    p = random.choice(base_pitches)
                    n = note.Note(p, quarterLength=d)
                    
                    # 依節奏長度加入表情記號
                    if d >= 1.0: n.articulations.append(articulations.Accent())
                    elif d <= 0.25: n.articulations.append(articulations.Staccato())
                    
                    lh_part.append(n)
                    curr_beat += d

                # --- 右手：伴奏 ---
                rh_pitches = [p.replace('2', '4').replace('1', '3') for p in chord_notes]
                # 第一拍重音，後三拍斷奏伴奏
                rh_part.append(chord.Chord(rh_pitches, quarterLength=1.0))
                for _ in range(3):
                    c_accomp = chord.Chord(rh_pitches, quarterLength=1.0)
                    c_accomp.articulations.append(articulations.Staccato())
                    rh_part.append(c_accomp)

def generate_final_strict_score(output_file):
    s = stream.Score()
    s.metadata = metadata.Metadata(title='80小節古典變奏曲(125 BPM)', composer='Python AI')
    
    # 設定速度 125
    s.append(tempo.MetronomeMark(number=125))

    rh = stream.Part(id='RH')
    rh.append(clef.TrebleClef())
    lh = stream.Part(id='LH')
    lh.append(clef.BassClef())
    lh.append(key.Key('C'))

    # 定義 4 個核心和弦 (C, Am, F, G)
    four_chord_prog = [
        ['C2','E2','G2'], # C Major
        ['A1','C2','E2'], # A Minor
        ['F1','A1','C2'], # F Major
        ['G1','B1','D2']  # G Major
    ]

    print("正在生成：80小節 / 2小節一和弦 / 125 BPM...")
    
    # 執行生成 80 小節 (共 10 個循環)
    add_strict_2_measure_chords(rh, lh, 80, four_chord_prog)

    # 加上完美的終止式
    lh.append(note.Note('C2', quarterLength=4.0))
    rh.append(chord.Chord(['C4', 'E4', 'G4'], quarterLength=4.0))

    s.insert(0, rh)
    s.insert(0, lh)

    s.write('musicxml', fp=output_file)
    print(f"成功！已生成完美結構樂譜：{output_file}")

if __name__ == "__main__":
    # 請確保資料夾空間充足
    generate_final_strict_score("final_piano_score_strict.xml")