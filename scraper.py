def extract_emails(html):
    """Extract standard and obfuscated emails from text, excluding example.com."""
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    # Standard format emails
    emails = set(re.findall(email_pattern, html))

    # Obfuscated formats
    obfuscation_patterns = [
        r'([a-zA-Z0-9._%+-]+)\s?(?:\[at\]|\(at\)| at | AT )\s*([a-zA-Z0-9.-]+)\s?(?:\[dot\]|\(dot\)| dot | DOT )\s*([a-zA-Z]{2,})'
    ]
    for pattern in obfuscation_patterns:
        for match in re.findall(pattern, html, re.IGNORECASE):
            user, domain, tld = match
            emails.add(f"{user}@{domain}.{tld}")

    # Filter out example.com
    return [email for email in emails if not email.lower().endswith('@example.com')]