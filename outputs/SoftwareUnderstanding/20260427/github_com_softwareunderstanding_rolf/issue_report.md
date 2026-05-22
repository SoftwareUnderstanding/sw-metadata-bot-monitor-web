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

**Repository:** https://github.com/SoftwareUnderstanding/rolf
**Analysis Date:** 2026-04-27
**sw-metadata-bot version:** 0.4.2
**RSMetacheck version:** 0.2.1

## 🔴 Pitfalls (2)

### [P001](https://w3id.org/rsmetacheck/catalog/#P001)
**Evidence:** P001 detected: pyproject.toml version '0.1.0' does not match release version '0.0.1-alpha'

**Suggestion:** Ensure the version in your metadata matches the latest official release (0.0.1-alpha). Keeping these synchronized avoids confusion for users and improves reproducibility.

### [P002](https://w3id.org/rsmetacheck/catalog/#P002)
**Evidence:** P002 detected: LICENSE file contains unreplaced template placeholders

**Suggestion:** Update the copyright section with accurate names, organizations, and the current year. Personalizing this section ensures clarity and legal accuracy.

## ⚠️ Warnings (1)

### [W001](https://w3id.org/rsmetacheck/catalog/#W001)
**Evidence:** W001 detected: pyproject.toml contains software requirements without versions: poetry-core

**Suggestion:** Add version numbers to your dependencies. This provides stability for users and allows reproducibility across different environments.

## 📄 Missing codemeta.json

No root `codemeta.json` file was detected in the repository. A generated suggestion is provided below.

```json
{
  "@context": "https://w3id.org/codemeta/3.0",
  "@type": [
    "SoftwareSourceCode",
    "SoftwareApplication"
  ],
  "license": {
    "name": "Apache License 2.0",
    "url": "https://raw.githubusercontent.com/SoftwareUnderstanding/rolf/main/LICENSE",
    "identifier": "https://spdx.org/licenses/Apache-2.0"
  },
  "codeRepository": "https://github.com/SoftwareUnderstanding/rolf",
  "issueTracker": "https://github.com/SoftwareUnderstanding/rolf/issues",
  "dateCreated": "2021-10-03",
  "dateModified": "2026-03-03",
  "downloadUrl": "https://github.com/SoftwareUnderstanding/rolf/releases",
  "name": "rolf",
  "keywords": [
    "classification",
    "methodology",
    "research-software",
    "taxonomic-classification"
  ],
  "programmingLanguage": [
    "Jupyter Notebook"
  ],
  "softwareRequirements": [
    {
      "name": "python",
      "@type": "SoftwareApplication",
      "version": "^3.12"
    },
    {
      "name": "pandas",
      "@type": "SoftwareApplication",
      "version": "^3.0.1"
    },
    {
      "name": "scikit-learn",
      "@type": "SoftwareApplication",
      "version": "1.5.0"
    },
    {
      "name": "logthis",
      "@type": "SoftwareApplication",
      "version": "^1.0.1"
    },
    {
      "name": "nltk",
      "@type": "SoftwareApplication",
      "version": "^3.9.2"
    },
    {
      "name": "inflect",
      "@type": "SoftwareApplication",
      "version": "^7.5.0"
    },
    {
      "name": "contractions",
      "@type": "SoftwareApplication",
      "version": "^0.1.73"
    },
    {
      "name": "bs4",
      "@type": "SoftwareApplication",
      "version": "^0.0.2"
    },
    {
      "name": "imblearn",
      "@type": "SoftwareApplication",
      "version": "^0.0"
    },
    {
      "name": "poetry-core",
      "@type": "SoftwareApplication"
    }
  ],
  "releaseNotes": "# ROLF - Research sOftware cLassification Framework\r\n\r\nThis is an early release of ROLF. The datasets are in their final versions and the user script is ready. Missing readme file.",
  "softwareVersion": "v0.0.1-alpha",
  "datePublished": "2022-05-13",
  "buildInstructions": [
    "https://raw.githubusercontent.com/SoftwareUnderstanding/rolf/main/README.md"
  ],
  "author": [
    {
      "@type": "Organization",
      "identifier": "SoftwareUnderstanding",
      "@id": "https://github.com/SoftwareUnderstanding"
    },
    {
      "@type": "Person",
      "name": "Jenifer Tabita Ciuciu-Kiss"
    },
    {
      "@type": "Person",
      "name": "Andr\u00e9s Montero"
    }
  ],
  "readme": "https://raw.githubusercontent.com/SoftwareUnderstanding/rolf/main/README.md",
  "runtimePlatform": "Python^3.12",
  "description": [
    "Implementation of a flexible methodology for research software classification"
  ]
}
```


---

This report was generated automatically by [sw-metadata-bot](https://github.com/SoftwareUnderstanding/sw-metadata-bot) on your main default branch.

If you're not interested in participating, please comment "unsubscribe" and we will remove your repository from our list.
If you would like the pitfalls and warnings to be fixed automatically, please comment "auto-fix" and we will prioritize adding this feature in future iterations.
