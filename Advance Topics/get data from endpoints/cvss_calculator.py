from cvss import CVSS3

def calculate_cvss_score(vector: str):
    """
    Calculate CVSS v3 Base Score and Severity from a vector string.
    
    Args:
        vector (str): A valid CVSS:3.0 or CVSS:3.1 vector string.
    
    Returns:
        dict: { 'base_score': float, 'severity': str }
    """
    try:
        cvss = CVSS3(vector)
        base_score = cvss.scores()[0]
        severity = cvss.severities()[0]
        return {
            'base_score': base_score,
            'severity': severity
        }
    except Exception as e:
        return {
            'error': f'Invalid CVSS vector or failed to parse: {e}'
        }

# Example usage
vector = "CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H"
result = calculate_cvss_score(vector)
print(result)
