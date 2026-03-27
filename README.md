# Phishing Detection Tool

## Overview

An automated Python-based security tool that analyzes URLs and email headers for phishing indicators. Designed for security professionals, GRC practitioners, and organizations implementing security awareness programs.

**Risk Scoring:** 0-100 scale with detailed findings and actionable recommendations.

## Features

### URL Analysis
- ✅ Detects typosquatting and domain mimicry
- ✅ Identifies homograph attacks (e.g., goog1e, micr0soft)
- ✅ Checks for suspicious characters (@, //) in URLs
- ✅ Validates SSL certificate usage (HTTPS vs HTTP)
- ✅ Detects IP address usage instead of domain names
- ✅ Analyzes URL length and suspicious keywords
- ✅ Assesses TLD reputation (flags free/suspicious TLDs)
- ✅ Compares against whitelist/blacklist databases

### Email Analysis
- ✅ Detects sender spoofing (From ≠ Return-Path)
- ✅ Identifies Reply-To mismatches
- ✅ Analyzes email headers for phishing indicators
- ✅ Flags suspicious keywords and urgency language
- ✅ Logs all analysis with timestamps

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Linux/Kali Linux (recommended) or Windows/macOS

### Setup (5 minutes)

**Option 1: Automated Setup**

```bash
git clone https://github.com/gauravmalhotra3300-hub/phishing-detector.git
cd phishing-detector
pip3 install -r requirements.txt
```

**Option 2: Manual Setup**

```bash
mkdir phishing-detector && cd phishing-detector
# Download all files or clone the repository
pip3 install requests beautifulsoup4 dnspython urllib3 colorama
```

## Usage

### Run the Tool

```bash
python3 phishing_detector.py
```

### Interactive Menu

The tool presents an interactive menu:

```
Options:
1. Analyze URL
2. Analyze Email
3. Exit

Select option (1-3): 
```

### Example 1: Analyze a Suspicious URL

```
Enter URL: http://goog1e.com/verify-account

[*] Analyzing URL: http://goog1e.com/verify-account
[!] @ symbol detected
[!] No HTTPS
[!] Suspicious TLD
[!] HOMOGRAPH ATTACK

==================================================
URL ANALYSIS REPORT
==================================================
URL: http://goog1e.com/verify-account
Risk Score: 85/100
Risk Level: CRITICAL

Findings:
  • URL Length: 33 chars
  • Suspicious Char: @ detected
  • SSL Certificate: NO HTTPS
  • Homograph Attack: CRITICAL - goog1e
```

### Example 2: Analyze a Safe URL

```
Enter URL: https://google.com

[*] Analyzing URL: https://google.com
[+] Whitelisted domain

Risk Score: 5/100
Risk Level: SAFE
Recommendation: ✅ LIKELY SAFE
```

## How It Works

### Risk Scoring Algorithm

Each phishing indicator adds points to the risk score (0-100):

| Indicator | Risk Points | Severity |
|-----------|------------|----------|
| No HTTPS | +20 | Medium |
| IP Address Used | +30 | High |
| Homograph Attack | +35 | Critical |
| Blacklisted Domain | +50 | Critical |
| @ Symbol in URL | +25 | High |
| Suspicious Keywords | +15 | Medium |
| Suspicious TLD | +15 | Medium |

### Risk Levels

- **SAFE (0-19):** ✅ Low risk, proceed normally
- **LOW (20-39):** ⚠️ Minor concerns, review carefully
- **MEDIUM (40-59):** ⚠️ Suspicious, verify sender
- **HIGH (60-79):** ⚠️ High risk, do not interact
- **CRITICAL (80-100):** ❌ Likely phishing, block immediately

## Architecture

```
phishing-detector/
├── phishing_detector.py       # Main program
├── config.py                  # Configuration & detection rules
├── modules/
│   ├── url_analyzer.py       # URL phishing detection
│   └── email_analyzer.py     # Email header analysis
├── logs/
│   └── analysis_log.txt      # Audit trail of analyses
├── reports/
│   └── [generated reports]   # HTML analysis reports
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## Use Cases

### 1. Security Awareness Training
Use to educate employees on phishing indicators during security training programs.

### 2. Incident Response
Quickly analyze suspicious URLs/emails during security incidents.

### 3. GRC & Compliance
Integrate into ISO 27001 A.7.2.2 (Security Awareness Training) programs to measure user security posture.

### 4. Email Security Filtering
Incorporate detection logic into email gateway rules.

### 5. Threat Intelligence
Build phishing indicator databases and track trends over time.

## Configuration

Edit `config.py` to customize:

- **WHITELIST_DOMAINS:** Add trusted domains
- **BLACKLIST_DOMAINS:** Add known phishing domains
- **SUSPICIOUS_KEYWORDS:** Customize detection keywords
- **SUSPICIOUS_TLDS:** Add/remove suspicious TLDs
- **RISK_LEVELS:** Adjust risk scoring thresholds

## Output Files

- **logs/analysis_log.txt:** Timestamped analysis history
- **reports/:** Generated HTML reports with visualizations

## Limitations

- Does not interact with external threat intelligence APIs
- Local analysis only (no internet connectivity required)
- Basic email analysis (header-based only)
- Does not access SSL certificate details remotely

## Requirements

```
requests==2.31.0
beautifulsoup4==4.12.2
dnspython==2.4.2
urllib3==2.0.7
colorama==0.4.6
```

## Development

### Testing

```bash
python3 phishing_detector.py

# Test URLs
- http://goog1e.com/verify  (Should be CRITICAL)
- https://google.com         (Should be SAFE)
- http://192.168.1.1         (Should be HIGH)
```

### Contributing

Contributions are welcome! Areas for enhancement:
- Integration with threat intel APIs (VirusTotal, URLhaus)
- Machine learning classification
- Browser plugin version
- REST API interface
- Advanced email parsing

## Career & Learning Value

This project demonstrates:

✅ **Cybersecurity Knowledge:**
- Phishing attack vectors and indicators
- Risk assessment and scoring
- Email security and header analysis

✅ **Python Development:**
- Object-oriented programming
- Module design and organization
- File I/O and logging
- CLI application development

✅ **GRC Skills:**
- Security awareness program design
- Risk and control assessment
- Compliance with ISO 27001 standards
- Audit trail and reporting

✅ **Security Operations:**
- Incident response procedures
- Threat analysis workflows
- Employee training programs

## License

MIT License - Free to use, modify, and distribute.

## Author

Gaurav Malhotra  
Cybersecurity Professional | GRC Specialist  
MSc Cyber Security, University of Derby  
ISO 27001 Certified

## Support

For questions, issues, or feature requests, please open an issue on GitHub.

---

**Disclaimer:** This tool is designed for authorized security testing and awareness training only. Unauthorized use of phishing detection or social engineering techniques is illegal. Always obtain proper authorization before conducting any security assessments.
