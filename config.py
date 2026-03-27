RISK_LEVELS = {'critical': (80, 100), 'high': (60, 79), 'medium': (40, 59), 'low': (20, 39), 'safe': (0, 19)}
SUSPICIOUS_KEYWORDS = ['verify', 'confirm', 'account', 'update', 'secure', 'click here', 'urgent', 'action required', 'suspended', 'locked', 'unusual activity', 'reset', 'validate', 'authenticate', 'approval', 're-enter']
BLACKLIST_DOMAINS = ['suspicious-domain.com', 'phishing-site.net', 'fake-bank.com']
WHITELIST_DOMAINS = ['google.com', 'microsoft.com', 'apple.com', 'amazon.com', 'facebook.com', 'linkedin.com', 'github.com']
LOG_FILE = 'logs/analysis_log.txt'
REPORT_DIR = 'reports/'
SUSPICIOUS_TLDS = ['.tk', '.ml', '.ga', '.cf', '.xyz', '.top', '.bid']
