from paper_retrieval import search_papers
from paper_parser import parse_pdf
from paper_merger import build_ablation_table

def run_pipeline(query: str):

    print("[Pipeline] Searching papers...")

    pdfs = search_papers(query)

    print("[Pipeline] Parsing papers...")

    structured = []
    for pdf in pdfs:
        structured.append(parse_pdf(pdf))

    print("[Pipeline] Merging ablation design...")

    result = build_ablation_table(structured)

    return result

   