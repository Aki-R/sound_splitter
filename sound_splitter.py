from pydub import AudioSegment
import os

def normalize_audio(audio):
    """
    音声ファイルの音量を正規化する関数
    """
    normalized_audio = audio.normalize()
    return normalized_audio

def split_audio(audio, chunk_length_ms):
    """
    音声ファイルを指定した長さで区切る関数
    """
    chunks = []
    for i in range(0, len(audio), chunk_length_ms):
        chunks.append(audio[i:i+chunk_length_ms])
    return chunks

def main(input_dir, output_dir):
    # 出力ディレクトリが存在しない場合は作成する
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 入力ディレクトリ内のすべてのファイルを処理する
    file_count = 0  # 出力ファイルの連番
    for filename in os.listdir(input_dir):
        if filename.endswith(".wav"):
            input_path = os.path.join(input_dir, filename)
            output_basename = os.path.splitext(filename)[0]  # 拡張子を除いたファイル名
            output_path_base = os.path.join(output_dir, output_basename)

            # 音声ファイルの読み込み
            audio = AudioSegment.from_wav(input_path)

            # 音声の正規化
            normalized_audio = normalize_audio(audio)

            # 10秒ごとに音声を区切る
            chunk_length_ms = 10000
            chunks = split_audio(normalized_audio, chunk_length_ms)

            # 区切った音声を保存する
            for i, chunk in enumerate(chunks):
                output_path = f"{output_dir}\{file_count}.wav"
                chunk.export(output_path, format="wav", parameters=["-ac", "1", "-ar", "44100"])
                file_count += 1

if __name__ == "__main__":
    input_dir = "C:/Users/Akira/Desktop/オンガム/material/only_voice"  # 入力ディレクトリのパスを指定
    output_dir = "C:/Users/Akira/Desktop/オンガム/train_data"  # 出力ディレクトリのパスを指定
    main(input_dir, output_dir)
