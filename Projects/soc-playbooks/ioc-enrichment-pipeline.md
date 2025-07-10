
# 🎯 Custom IOC Enrichment Pipeline with Microsoft Sentinel

>This project establishes a custom IOC enrichment pipeline within Microsoft Sentinel, automating the enhancement of Indicators of Compromise (IOCs) using external threat intelligence sources like VirusTotal and AbuseIPDB. The pipeline ingests IOCs from Sentinel alerts, enriches them through API queries, and updates the original alerts with severity levels and threat actor tags when available. Triggered by Sentinel alerts, the Logic App parses the IOCs, analyzes the enrichment results, and can optionally notify analysts via Teams or Slack. This solution enhances threat detection and response capabilities while ensuring that Microsoft Sentinel and Logic Apps are in the same region or properly linked.

## 🛠 Tools & Services Used
- **Microsoft Sentinel**
- **Logic App (Playbook)**
- **VirusTotal API**
- **AbuseIPDB API**

## 🚀 Overview

This playbook automates the enrichment of Indicators of Compromise (IOCs) within Microsoft Sentinel using external threat intelligence sources.

### 🎯 Objectives
- Ingest IOCs directly from Microsoft Sentinel alerts.
- Automatically enrich IOCs (IP addresses, domains, URLs, hashes) using:
  - VirusTotal
  - AbuseIPDB
- Update the original alert with:
  - Severity based on enrichment
  - Threat actor or campaign tags (if available)

---

![image](https://github.com/user-attachments/assets/35e6b294-7e6c-48c3-9032-21779532c8f2)


## 🔁 Workflow

1. **Trigger**: Sentinel alert triggers the Logic App.
2. **Extract**: Parse the alert for IOCs (IP, domain, hash, URL).
3. **Enrich**:
   - Query VirusTotal API
   - Query AbuseIPDB API (for IPs)
4. **Analyze**:
   - Assign severity (e.g., high if malicious flag count > threshold)
   - Attempt mapping to known threat actors (via tags or VT metadata)
5. **Update**:
   - Add custom tags to the original alert
   - Optionally forward to Teams/Slack for analyst triage

---

## 🔐 API Keys Required

- **VirusTotal API Key**: [https://www.virustotal.com/gui/join-us](https://www.virustotal.com/gui/join-us)
- **AbuseIPDB API Key**: [https://www.abuseipdb.com/account/api](https://www.abuseipdb.com/account/api)

---
![image](https://github.com/user-attachments/assets/124a762d-5401-4887-b812-cb8880163fb9)


> ⚠ Make sure Sentinel and Logic Apps are in the same region or linked across regions.
