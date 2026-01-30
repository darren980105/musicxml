這是一項可以生成鋼琴伴奏的古典樂的程式
1. 環境需求
確保你的電腦已安裝 Python 3.x 以及 music21 套件：
pip install music21
2. 下載與執行
將專案複製到本地後，執行主程式：
python final_piano_score_strict.py 
3.執行成功後，資料夾內會出現 final_piano_score_strict.xml 檔案
[A]本程式透過 music21 的 stream 模組構建雙聲部：
  (右手)：負責提供和聲支持，音域位於 C4-G5
  (左手)：作為主角，負責主旋律，音域位於 C2-C4
[B]完整樂曲結構：自動生成 80 小節的完整樂譜，具備起承轉合。
[C]125 BPM 曲速：預設快板速度。
[D]樂句風格變換：每8小節自動更換一次旋律性格。
[E]嚴謹和弦進行：採用C-Am-F-G循環，每個和弦固定持續2小節。
[F]自動標註重音（Accent）與斷奏（Staccato）。
[G]右手採用「首拍強音+後三拍斷奏」的鋼琴伴奏。
[H]高度相容性：輸出格式為 MusicXML，可完美匯入Flat.io、MuseScore、Sibelius等軟體。
