import os
import subprocess
import glob
import re

def get_pdf_info(filepath):
    """Gets PDF info using pdfinfo."""
    try:
        result = subprocess.run(['pdfinfo', filepath], capture_output=True, text=True, check=True)
        return result.stdout
    except Exception:
        return ""

def get_pdf_text(filepath, page=1):
    """Extracts text from a specific page using pdftotext."""
    try:
        result = subprocess.run(['pdftotext', '-f', str(page), '-l', str(page), filepath, '-'], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except Exception:
        return ""

def ocr_page(filepath, page=1):
    """OCRs the first page of a PDF using pdftoppm and tesseract."""
    try:
        # Convert first page to image (PPM)
        ppm_prefix = f"/tmp/pdf_page_{os.getpid()}"
        subprocess.run(['pdftoppm', '-f', str(page), '-l', str(page), '-singlefile', filepath, ppm_prefix], check=True)
        
        # OCR the image
        img_path = f"{ppm_prefix}.ppm"
        if not os.path.exists(img_path):
            return ""
            
        result = subprocess.run(['tesseract', img_path, '-', '-l', 'ita'], capture_output=True, text=True, check=True)
        
        # Cleanup
        os.remove(img_path)
        
        return result.stdout.strip()
    except Exception as e:
        print(f"Error OCRing {filepath}: {e}")
        return ""

def extract_topic(filepath):
    """Tries to find a topic for the PDF."""
    # First, check filename (cleaned up)
    basename = os.path.basename(filepath)
    filename_topic = re.sub(r'^(Copy of |Lezione |Copy Of )', '', basename, flags=re.IGNORECASE)
    filename_topic = filename_topic.replace('.pdf', '').strip()
    
    # Try getting text (digital)
    text = get_pdf_text(filepath, page=1)
    if text and len(text) > 20:
        # Extract first line as possible title
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        if lines:
            return lines[0]
    
    # Try OCR (scanned)
    ocr_text = ocr_page(filepath, page=1)
    if ocr_text:
        lines = [l.strip() for l in ocr_text.split('\n') if l.strip()]
        if lines:
            # Filter out small noise
            for line in lines[:3]:
                if len(line) > 5:
                    return line
                    
    return filename_topic

def main():
    pdf_files = sorted(glob.glob("*.pdf"))
    index_content = "# Indice Analisi 1\n\n"
    
    for pdf in pdf_files:
        print(f"Analyzing {pdf}...")
        topic = extract_topic(pdf)
        # Handle cases where topic might contain characters that break markdown links
        display_topic = topic.replace('[', '').replace(']', '').replace('|', '-')
        
        index_content += f"## [[{pdf}|{display_topic}]]\n"
        index_content += f"- [Apri PDF]([[{pdf}]])\n"
        
        # If it's a "Lezione", maybe adding page 1 link
        index_content += f"- [Inizio slide]([[{pdf}#page=1]])\n\n"
        
    with open("Indice Analisi 1.md", "w") as f:
        f.write(index_content)
    
    print("Index generated: Indice Analisi 1.md")

if __name__ == "__main__":
    main()
