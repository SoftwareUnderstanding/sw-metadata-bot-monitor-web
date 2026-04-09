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

**Repository:** https://github.com/SoftwareUnderstanding/somef_server
**Analysis Date:** 2026-04-09
**sw-metadata-bot version:** 0.4.1
**RSMetacheck version:** 0.2.1

## 🔴 Pitfalls (1)

### [P002](https://w3id.org/rsmetacheck/catalog/#P002)
**Evidence:** P002 detected: LICENSE file contains unreplaced template placeholders

**Suggestion:** Update the copyright section with accurate names, organizations, and the current year. Personalizing this section ensures clarity and legal accuracy.

## ⚠️ Warnings (1)

### [W002](https://w3id.org/rsmetacheck/catalog/#W002)
**Evidence:** W002 detected: codemeta.json dateModified '2025-03-28T00:00:00' is outdated compared to repository date '2026-02-13T17:01:34'

**Suggestion:** The data in the metadata file should be updated to be aligned with the date of the latest release. Automating this synchronization as part of your release process is highly recommended.


---

This report was generated automatically by [sw-metadata-bot](https://github.com/SoftwareUnderstanding/sw-metadata-bot).

If you're not interested in participating, please comment "unsubscribe" and we will remove your repository from our list.
