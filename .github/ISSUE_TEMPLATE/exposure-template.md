---
name: Exposure report template
about: Template to report a exposure in RVD. See https://bit.ly/2JnamaD if in doubt
title: ''
labels: exposure
assignees: ''

---

# Exposure report

### Summary table
| Input      | Value  |
|---------|--------|
| Robot `OR` Robot component | <ins>`required`</ins> |
| Vendor  | `optional`  |
| CVE ID  | `optional`, if exists  |
| CWE ID  | <ins>`required`</ins>, refer to https://cwe.mitre.org/data/pdf/1000_abstraction_colors.pdf for help  |
| Module URL | 	`optional`, *link to docker image to reproduce flaw* |
| Attack vector | <ins>`required`</ins> e.g.: Local network or Physical access |

### Description:

*Please provide a brief description of the exposure and how to reproduce it. Refer to https://github.com/aliasrobotics/RVD#appendix-a-vulnerabilities-weaknesses-bugs-and-more if you need clarifications on the terminology*