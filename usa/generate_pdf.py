import subprocess
import os
import sys
import time

html_path = os.path.abspath(r"C:\Users\mserv\Desktop\Marta\Github\cortag-reports\usa\cortag_report_usa_T1_2026.html")
pdf_path  = os.path.abspath(r"C:\Users\mserv\Desktop\Marta\Github\cortag-reports\usa\cortag_report_usa_T1_2026.pdf")

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

file_url = "file:///" + html_path.replace("\\", "/")

cmd = [
    chrome,
    "--headless=new",
    "--disable-gpu",
    "--no-sandbox",
    "--disable-software-rasterizer",
    "--disable-dev-shm-usage",
    "--run-all-compositor-stages-before-draw",
    "--no-pdf-header-footer",
    "--print-to-pdf-no-header",
    f"--print-to-pdf={pdf_path}",
    "--virtual-time-budget=4000",
    file_url
]

print(f"Generando PDF desde:\n  {html_path}")
print(f"Destino:\n  {pdf_path}\n")

result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)

if os.path.exists(pdf_path):
    size_kb = os.path.getsize(pdf_path) / 1024
    print(f"PDF generado correctamente: {size_kb:.0f} KB")
    print(f"Ruta: {pdf_path}")
else:
    print("ERROR: no se generó el PDF")
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    sys.exit(1)
