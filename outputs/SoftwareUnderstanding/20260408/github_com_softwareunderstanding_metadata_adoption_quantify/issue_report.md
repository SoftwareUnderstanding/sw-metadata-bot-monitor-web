You are part of the Software Understanding metadata quality initiative. Several metadata issues were identified and could be addressed.

This automated issue includes:
- Detected metadata pitfalls and warnings
- Suggestions for fixing each issue

## Context
This analysis is performed by the [CodeMetaSoft](https://w3id.org/codemetasoft) project to help improve research software quality.

This is a first initiative aimed at identifying and reporting metadata quality issues across research software repositories. 
At this stage, we only provide diagnostics and recommendations. 
In future iterations, we plan to propose automated fixes for the detected issues to further simplify the improvement process and reduce manual effort.

Each pitfall and warning is identified by a unique code (e.g. P001 for pitfalls, W004 for warnings) that corresponds to specific metadata quality issues.
You can find more details about these checks and how to address them in the [RSMetacheck catalog](https://github.com/SoftwareUnderstanding/RSMetacheck/blob/main/catalog.md).


# Metadata Quality Report

**Repository:** https://github.com/SoftwareUnderstanding/Metadata-Adoption-Quantify
**Analysis Date:** 2026-04-08
**sw-metadata-bot version:** 0.4.0
**RSMetacheck version:** 0.2.1

## 🔴 Pitfalls (4)

### [P001](https://w3id.org/rsmetacheck/catalog/#P001)
**Evidence:** P001 detected: codemeta.json version '1.0.0' does not match release version '2.0.0'

**Suggestion:** Ensure the version in your metadata matches the latest official release. Keeping these synchronized avoids confusion for users and improves reproducibility.

### [P002](https://w3id.org/rsmetacheck/catalog/#P002)
**Evidence:** P002 detected: LICENSE file contains unreplaced template placeholders

**Suggestion:** Update the copyright section with accurate names, organizations, and the current year. Personalizing this section ensures clarity and legal accuracy.

### [P014](https://w3id.org/rsmetacheck/catalog/#P014)
**Evidence:** P014 detected: codemeta.json Identifier uses bare DOI instead of full URL: '10.5281/zenodo.14803019'

**Suggestion:** You should include the full DOI URL form in your metadata (e.g., https://doi.org/XX.XXXX/zenodo.XXXX)

### [P016](https://w3id.org/rsmetacheck/catalog/#P016)
**Evidence:** P016 detected: codeRepository points to different repository: https://github.com/SoftwareUnderstanding/Metadata-Adoption-Quantify

**Suggestion:** Make sure that the codeRepository URL in your metadata exactly matches the repository hosting your source code.

## ⚠️ Warnings (1)

### [W004](https://w3id.org/rsmetacheck/catalog/#W004)
**Evidence:** W004 detected: codemeta.json Programming languages without versions: Python3

**Suggestion:** Include version numbers for each programming language used. Defining these helps ensure reproducibility and compatibility across systems.


---

This report was generated automatically by [sw-metadata-bot](https://github.com/SoftwareUnderstanding/sw-metadata-bot).

If you're not interested in participating, please comment "unsubscribe" and we will remove your repository from our list.
