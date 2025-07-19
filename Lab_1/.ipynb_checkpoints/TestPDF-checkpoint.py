import nbformat
from nbconvert import PDFExporter
import os

print("Testing PDF generation capabilities...")

# Test LaTeX availability
try:
    import subprocess
    result = subprocess.run(['pdflatex', '--version'], 
                          capture_output=True, text=True)
    if result.returncode == 0:
        print("✓ LaTeX/PDFLaTeX is available")
    else:
        print("✗ LaTeX not found")
except:
    print("✗ LaTeX not available")

# Test nbconvert PDF export
try:
    exporter = PDFExporter()
    print("✓ nbconvert PDF exporter is available")
except Exception as e:
    print(f"✗ nbconvert PDF exporter error: {e}")

# Test WeasyPrint (alternative PDF generator)
try:
    import weasyprint
    print("✓ WeasyPrint is available")
except Exception as e:
    print(f"✗ WeasyPrint error: {e}")

# Test ReportLab (programmatic PDF creation)
try:
    from reportlab.pdfgen import canvas
    print("✓ ReportLab is available")
except Exception as e:
    print(f"✗ ReportLab error: {e}")

print("PDF generation test complete!")
