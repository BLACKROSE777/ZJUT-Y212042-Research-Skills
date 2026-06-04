def build_ablation_table(papers):

    header = "| Paper | Dataset | Metric | Ablation Option | Evidence Strength |"
    sep = "|------|--------|--------|------------------|------------------|"

    table = [header, sep]

    for p in papers:
        paper = p["paper"]
        datasets = ",".join(p.get("datasets", []))
        metrics = ",".join(p.get("metrics", []))

        for ab in p["ablation_candidates"]:

            # simple confidence heuristic
            if "attention" in ab or "backbone" in ab:
                confidence = "HIGH"
            else:
                confidence = "MEDIUM"

            table.append(
                f"| {paper} | {datasets} | {metrics} | {ab} | {confidence} |"
            )

    return "\n".join(table)