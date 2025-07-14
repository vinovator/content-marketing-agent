# src/app/tabs/export_tab.py

import streamlit as st
from pathlib import Path
from datetime import datetime
import os
import re

from docx import Document
from fpdf import FPDF

# --- Utility Functions ---

def slugify(text):
    return re.sub(r'[\W_]+', '_', text.strip().lower())

def get_filename(title, ext):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{timestamp}_{slugify(title)}.{ext}"

def write_markdown(title, metadata, content):
    return f"# {title}\n\n" + \
           f"**Tone**: {metadata.get('tone', '-')}\n\n" + \
           f"**Audience**: {metadata.get('audience', '-')}\n\n" + \
           f"**Call to Action**: {metadata.get('cta', '-')}\n\n" + \
           "---\n\n" + content

def export_txt(filepath, content):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

def export_md(filepath, content):
    export_txt(filepath, content)  # same as txt

def export_docx(filepath, title, metadata, content):
    doc = Document()
    doc.add_heading(title, 0)
    doc.add_paragraph(f"Tone: {metadata.get('tone', '-')}")
    doc.add_paragraph(f"Audience: {metadata.get('audience', '-')}")
    doc.add_paragraph(f"Call to Action: {metadata.get('cta', '-')}")
    doc.add_paragraph("")  # spacer
    doc.add_paragraph(content)
    doc.save(filepath)

def export_pdf(filepath, title, metadata, content):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.multi_cell(0, 10, title)

    pdf.set_font("Arial", '', 12)
    pdf.ln(4)
    pdf.multi_cell(0, 10, f"Tone: {metadata.get('tone', '-')}")
    pdf.multi_cell(0, 10, f"Audience: {metadata.get('audience', '-')}")
    pdf.multi_cell(0, 10, f"Call to Action: {metadata.get('cta', '-')}")
    pdf.ln(5)

    pdf.multi_cell(0, 10, content)
    pdf.output(filepath)

# --- Main Tab Function ---

def render_export_tab():
    st.header("Step 8: Export Final Content")
    st.info("Download your polished content in Markdown, PDF, Word, or Plain Text formats.")

    export_dir = Path("/mnt/data/exports")
    export_dir.mkdir(parents=True, exist_ok=True)

    polished_drafts = st.session_state.get("final_export_ready", [])

    if not polished_drafts:
        st.warning("⚠️ No drafts selected for export. Please complete Step 7: Polish Content.")
        return

    for i, draft in enumerate(polished_drafts):
        st.markdown("---")
        st.subheader(f"📄 {draft['title']}")

        title = draft.get("title", f"Draft_{i+1}")
        content = draft.get("polished", "")
        brief = draft.get("brief", {})
        metadata = {
            "tone": brief.get("tone", "Professional"),
            "audience": brief.get("audience", "Business Leaders"),
            "cta": brief.get("cta", "")
        }

        md_content = write_markdown(title, metadata, content)

        # Export paths
        md_path = export_dir / get_filename(title, "md")
        txt_path = export_dir / get_filename(title, "txt")
        docx_path = export_dir / get_filename(title, "docx")
        pdf_path = export_dir / get_filename(title, "pdf")

        # Write files
        export_md(md_path, md_content)
        export_txt(txt_path, md_content)
        export_docx(docx_path, title, metadata, content)
        export_pdf(pdf_path, title, metadata, content)

        # Download Buttons
        st.download_button("⬇️ Download Markdown (.md)", data=md_path.read_bytes(), file_name=md_path.name)
        st.download_button("⬇️ Download Text (.txt)", data=txt_path.read_bytes(), file_name=txt_path.name)
        st.download_button("⬇️ Download Word (.docx)", data=docx_path.read_bytes(), file_name=docx_path.name)
        st.download_button("⬇️ Download PDF (.pdf)", data=pdf_path.read_bytes(), file_name=pdf_path.name)