from abc import ABC, abstractmethod
from google import genai
from google.genai import types
import pathlib

# === ABSTRACT BASE CLASS ===
class ImageAnalyzer(ABC):
    @abstractmethod
    def analyze(self, image_path: str, prompt: str) -> str:
        pass

# === IMPLEMENTASI KONKRET ===
class GeminiAnalyzer(ImageAnalyzer):
    def __init__(self, api_key: str, model_name="gemini-2.0-flash"):
        self.client = genai.Client(api_key=api_key)
        self.model_name = model_name

    def analyze(self, image_path: str, prompt: str) -> str:
        image_data = pathlib.Path(image_path).read_bytes()  
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=[
                types.Part.from_bytes(data=image_data, mime_type='image/*'),
                prompt
            ]
        )
        return response.text

# === FUNGSI UTAMA ===
def main():
    image_path = "./Rhplot.png"  # Pastikan file ini benar-benar ada
    prompt = "Analisis gambar ini dan berikan narasi sebagaimana anda adalah pembawa acara dalam info cuaca."

    analyzer: ImageAnalyzer = GeminiAnalyzer(api_key="AIzaSyDakjEg5aE3KXPdZwAcBuZ3ohiQICm7DHE")
    hasil = analyzer.analyze(image_path, prompt)

    print("=== Hasil Analisis ===")
    print(hasil)

    with open("hasil_analisis_gambar.txt", "w", encoding="utf-8") as f:
        f.write(hasil)

    print("Hasil analisis telah disimpan di 'hasil_analisis_gambar.txt'.")

if __name__ == "__main__":
    main()
