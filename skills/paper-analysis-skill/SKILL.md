---
name: paper-analysis-skill
version: 0.1.0
description: Structured multi-paper analysis from arXiv queries
type: research-skill
tags:
  - arxiv
  - ml
  - cv
  - paper-analysis
  - ablation
input: natural language research query
output: structured comparison table + analysis report
entry: entry.py
---

# Paper Analysis Skill

## 1. Purpose
This skill performs structured multi-paper analysis from arXiv queries.

## 2. Input
- natural language query (e.g., "2025 transformer object detection")

## 3. Output
- Top-5 papers
- structured paper attributes
- cross-paper comparison table
- ablation-style inference suggestions

## 4. Pipeline
1. Query arXiv
2. Retrieve top-5 papers
3. Parse paper summaries
4. Extract structured fields
5. Cross-paper aggregation

## 5. Reliability
- outputs are traceable to arXiv metadata
- each paper includes URL evidence
- comparison is deterministic aggregation

## 6. Limitation
- full PDF parsing not enabled yet
- dataset/metric extraction heuristic-based