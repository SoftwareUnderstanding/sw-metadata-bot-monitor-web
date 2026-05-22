You are part of the Software Understanding metadata quality initiative beta analysis. This initiative is meant to test the use of a bot to monitor the quality of metadata in software repositories.

This automated issue includes:
- Detected metadata pitfalls and warnings
- A suggested codemeta.json when no codemeta.json was detected
- Suggestions for fixing each issue

## Context
This analysis is performed by the [CodeMetaSoft](https://w3id.org/codemetasoft) project to help improve research software metadata quality.

This is a first initiative aimed at identifying and reporting metadata quality issues across research software repositories. 
At this stage, we only provide diagnostics and recommendations. 
In future iterations, we plan to propose automated fixes for the detected issues to further simplify the improvement process and reduce manual effort.

Each pitfall and warning is identified by a unique code (e.g. P001 for pitfalls, W004 for warnings) that corresponds to specific metadata quality issues.
You can find more details about these checks and how to address them in the [RSMetacheck catalog](https://softwareunderstanding.github.io/RsMetaCheck/).


# Metadata Quality Report

**Repository:** https://github.com/cds-astro/aladin-lite
**Analysis Date:** 2026-05-22
**sw-metadata-bot version:** 0.4.3
**RSMetacheck version:** 0.3.1

## 🔴 Pitfalls (2)

### [P002](https://w3id.org/rsmetacheck/catalog/#P002)
**Evidence:** P002 detected: LICENSE file contains unreplaced template placeholders

**Suggestion:** Update the copyright section with accurate names, organizations, and the current year. Personalizing this section ensures clarity and legal accuracy.

### [P014](https://w3id.org/rsmetacheck/catalog/#P014)
**Evidence:** P014 detected: metadata files Identifier uses bare DOI instead of full URL: '10.5281/zenodo.7638833'

**Suggestion:** You should include the full DOI URL form in your metadata (e.g., https://doi.org/10.5281/zenodo.7638833)

## ⚠️ Warnings (3)

### [W002](https://w3id.org/rsmetacheck/catalog/#W002)
**Evidence:** W002 detected: metadata files dateModified '2023-01-31T00:00:00' is outdated compared to repository date '2026-04-30T06:18:59'

**Suggestion:** The data in the metadata file should be updated to be aligned with the date of the latest release (2026-04-30T06:18:59).

### [W003](https://w3id.org/rsmetacheck/catalog/#W003)
**Evidence:** W003 detected: Repository has multiple licenses but metadata files only lists one. Found in: https://raw.githubusercontent.com/cds-astro/aladin-lite/master/LICENSE

**Suggestion:** Make sure you are using the correct licenses. This avoids confusion about terms of use and ensures full transparency.

### [W004](https://w3id.org/rsmetacheck/catalog/#W004)
**Evidence:** W004 detected: metadata files Programming languages without versions: Rust, Javascript

**Suggestion:** Include version numbers for each programming language used. Defining these helps ensure reproducibility and compatibility across systems.


---

This report was generated automatically by [sw-metadata-bot](https://github.com/SoftwareUnderstanding/sw-metadata-bot) on your main default branch.

If you're not interested in participating, please comment "unsubscribe" and we will remove your repository from our list.
If you would like the pitfalls and warnings to be fixed automatically, please comment "auto-fix" and we will prioritize adding this feature in future iterations.
