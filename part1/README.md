# HBnB Evolution - Part 1 (UML & Diagrams)

This directory contains the UML deliverables for **HBnB Evolution - Part 1**.
All diagrams are authored using **Mermaid** and stored as `.mmd` sources.

---

## Contents

- Overview
- Diagrams
- How to Render (Mermaid Online)
- Deliverables Checklist

---

## Overview

Part 1 focuses on defining the system blueprint:
- Layered architecture (Presentation, Business Logic, Persistence)
- Core domain entities (User, Place, Review, Amenity)
- Key user scenarios captured in a sequence diagram

---

## Diagrams

### 00) High-Level Package Diagram
- Source: `diagrams/00_high_level_package.mmd`

Purpose:
- Visualize layers and dependencies across the application

### 01) Business Logic Class Diagram
- Source: `diagrams/01_business_logic_class.mmd`

Purpose:
- Detail entity attributes, behaviors, and relationships

### 02) Sequence Diagram (All Scenarios in One)
- Source: `diagrams/02_sequence_all_scenarios.mmd`

Scenarios included:
- User registration
- Place creation
- Review submission
- Fetching list of places

---

## How to Render (Mermaid Online)

Use the Mermaid Online editor:
- Paste the `.mmd` content
- Export as SVG (recommended) and optionally PNG
- Save exported files beside the source if your checker requires images

---

## Deliverables Checklist

- [x] Mermaid sources for all required diagrams
- [x] Single sequence diagram file containing all scenarios
- [x] Task 03 documentation placeholder created: `documentation/03_documentation.md`
- [ ] Exported SVG/PNG (if required by the project PDF)
