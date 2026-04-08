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

**Repository:** https://github.com/SoftwareUnderstanding/rolf
**Analysis Date:** 2026-04-08
**sw-metadata-bot version:** 0.4.0
**RSMetacheck version:** 0.2.1

## 🔴 Pitfalls (2)

### [P001](https://w3id.org/rsmetacheck/catalog/#P001)
**Evidence:** P001 detected: pyproject.toml version '0.1.0' does not match release version '0.0.1-alpha'

**Suggestion:** Ensure the version in your metadata matches the latest official release. Keeping these synchronized avoids confusion for users and improves reproducibility.

### [P002](https://w3id.org/rsmetacheck/catalog/#P002)
**Evidence:** P002 detected: LICENSE file contains unreplaced template placeholders

**Suggestion:** Update the copyright section with accurate names, organizations, and the current year. Personalizing this section ensures clarity and legal accuracy.

## ⚠️ Warnings (1)

### [W001](https://w3id.org/rsmetacheck/catalog/#W001)
**Evidence:** W001 detected: pyproject.toml contains software requirements without versions: poetry-core

**Suggestion:** Add version numbers to your dependencies. This provides stability for users and allows reproducibility across different environments.


---

This report was generated automatically by [sw-metadata-bot](https://github.com/SoftwareUnderstanding/sw-metadata-bot).

If you're not interested in participating, please comment "unsubscribe" and we will remove your repository from our list.
