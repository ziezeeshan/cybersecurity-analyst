# 🔍 APT Lateral Movement Detection Lab (MITRE TTP Mappings)

## 📌 Objective

To simulate **APT-style lateral movement techniques** in a controlled lab environment, and build **MITRE ATT&CK-aligned detection rules** using Elastic Security and Splunk Enterprise Security.

This project is designed to emulate real-world attacker behavior from groups such as APT29, FIN6, or Cobalt Group, and create defensive content that maps directly to the ATT&CK framework.

---

## ⚔️ Simulated Techniques

| MITRE ID | Technique                        | Description                                 |
|----------|----------------------------------|---------------------------------------------|
| T1021.002 | SMB/Windows Admin Shares         | Using `psexec`, `wmic`, `net use`           |
| T1059.001 | PowerShell                       | Remote execution, reconnaissance             |
| T1071.001 | Application Layer Protocol: Web  | C2 beaconing via HTTP(S)                    |
| T1086     | Registry Run Keys                | Persistence method                          |
| T1003     | OS Credential Dumping            | Using mimikatz / lsass dump                 |

---

## 🧪 Lab Setup

- **Target**: Windows Server 2019 (DC), Windows 10 (Workstation)
- **Attacker VM**: Kali Linux + Covenant C2 / Metasploit
- **SIEM Stack**:
  - Elastic Stack 8.x (Beats + Fleet)
  - Splunk Enterprise Security 9.x
  - MITRE ATT&CK Navigator

---

## 🛠️ Tools Used

| Category           | Tool                         |
|--------------------|------------------------------|
| Logging & SIEM     | Elastic, Splunk ES           |
| Agent Telemetry    | Winlogbeat, Sysmon, Osquery  |
| Detection Rules    | Sigma, KQL, SPL              |
| Simulation Tools   | Atomic Red Team, Caldera     |
| Correlation Engine | MITRE ATT&CK Navigator       |

---

## 📊 Detection Engineering Process

1. **Simulate** attacker behavior using [Atomic Red Team](https://github.com/redcanaryco/atomic-red-team) and [Caldera](https://github.com/mitre/caldera)
2. **Collect logs** via Winlogbeat/Sysmon into Elastic + Splunk
3. **Correlate** alerts to MITRE TTPs
4. **Develop rules** in:
   - 🔹 `Sigma`
   - 🔹 `Elastic KQL`
   - 🔹 `Splunk SPL`
5. **Validate** detections via repeat executions
6. **Map** each rule to ATT&CK using Navigator JSON

---

## 📁 Project Files

