import re
from pdfminer.high_level import extract_text

def parse_pdf(pdf_path: str):

    text = extract_text(pdf_path)

    text_lower = text.lower()

    # -------- evidence-based extraction --------

    methods = []
    if "transformer" in text_lower:
        methods.append("transformer")
    if "cnn" in text_lower:
        methods.append("cnn")

    datasets = re.findall(r"(coco|imagenet|cifar-10|cifar-100)", text_lower)
    datasets = list(set(datasets)) if datasets else ["unknown"]

    metrics = []
    if "map" in text_lower:
        metrics.append("mAP")
    if "accuracy" in text_lower:
        metrics.append("accuracy")

    # -------- ablation reasoning (rule-based seed) --------

    ablation_candidates = []

    if "attention" in text_lower:
        ablation_candidates.append("remove attention module")

    if "backbone" in text_lower:
        ablation_candidates.append("remove backbone")

    if "head" in text_lower:
        ablation_candidates.append("replace detection head")

    if not ablation_candidates:
        ablation_candidates = ["remove key module (unknown)"]

    return {
        "paper": pdf_path,
        "text_length": len(text),
        "methods": methods,
        "datasets": datasets,
        "metrics": metrics,
        "ablation_candidates": ablation_candidates,
        "evidence": {
            "method_hits": methods,
            "dataset_hits": datasets,
            "metric_hits": metrics
        }
    }