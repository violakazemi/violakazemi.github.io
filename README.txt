# Viola Kazemi | Product Design Portfolio

> A custom-built, highly responsive portfolio showcasing systems-driven product design, AI-native interfaces, and UX case studies.

🌍 **Live Site:** [violakazemi.com](https://violakazemi.com)

## 📌 Overview

This repository contains the source code for my personal product design portfolio. As a product designer with a background in Computer Engineering, I approached the development of this site as its own UX/UI case study. 

The site is built with a custom, zero-framework CSS architecture. It utilizes an intrinsic, auto-reflowing CSS Grid system (`.bento-grid`, `.hero-grid`, `.footer-grid`) and a strict, Apple-inspired monochrome design token system to ensure the interface remains invisible while the case study work stands out.

## 🛠 Tech Stack & Architecture

* **Semantic HTML5:** Clean, accessible markup without heavily nested legacy wrapper `div`s.
* **Modern CSS3:** 
  * **Fluid Typography:** Scales seamlessly across all viewports using CSS `clamp()`.
  * **Intrinsic Grid Systems:** Uses `auto-fit` and `minmax()` to create responsive layouts that require zero media queries for standard breakpoints.
  * **CSS Variables:** A central `:root` token system controls the entire site's spacing (`--space-1` through `--space-8`), color palette, and elevation shadows.
* **Vanilla JavaScript:** Minimal JS used solely for essential UI interactions (like carousel navigation).
* **Zero Dependencies:** No Bootstrap, Tailwind, or heavy layout frameworks. 

## 📂 Featured Case Studies & Projects

The portfolio highlights a range of end-to-end design work, categorized into full UX case studies and concept labs:

**Featured Projects:**
* **The Museum Companion:** Research-driven educator dashboard and logistics calculator.
* **Golaab:** A custom e-commerce keepsakes builder focusing on artwork intent isolation.
* **Mechmarket:** A mobile community marketplace balancing enthusiast trust with rapid checkout.

**Design Lab (AI Integrations):**
* **Tomaan:** Reimagining offline-first security and latency-aware interfaces for the AI-native era.
* **Designing Inside Carbon:** A concept redesign proposing a compare-view within IBM watsonx's Prompt Lab.
