import cv2
import numpy as np

def preprocess_image(image_path):
    # Fotoğrafı yükleme
    image = cv2.imread(image_path)

    # Gri seviye
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Eşikleme 
    _, thresholded_image = cv2.threshold(gray_image, 181, 255, cv2.THRESH_BINARY)

    # Arka planları temizleme
    kernel = np.ones((5, 5), np.uint8)
    morph_image = cv2.morphologyEx(thresholded_image, cv2.MORPH_OPEN, kernel)

    return image, gray_image, thresholded_image, morph_image

def count_and_display_rice_grains(original_image, thresholded_image, morph_image):
    # Sayma ve etiketleme işlemi
    _, labels, stats, _ = cv2.connectedComponentsWithStats(morph_image, connectivity=8)

    # Pirinç Tanelerinin sayısını ekrana yazdırma
    rice_count = len(stats) - 1  # İlk etiket arka plan olduğu için çıkarılır
    print(f"Pirinç Tanelerinin Sayısı: {rice_count}")

    # Görüntüyü ekrana yazdır
    cv2.imshow('orjinal resim', original_image)
    cv2.imshow('eşiklenmiş goruntu', thresholded_image)
    cv2.imshow('temizlenmi goruntu', morph_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if _name_ == "_main_":
    image_path = r"C:\Users\Hilemnur\Downloads\Hilem.jpg"
    
    original_image, gray_image, thresholded_image, morph_image = preprocess_image(image_path)
    count_and_display_rice_grains(original_image, thresholded_image, morph_image)
