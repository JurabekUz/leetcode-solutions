class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        clean_emails = []

        for email in emails:
            parts = email.split("@")
            local = parts[0].split("+")[0]
            clean_emails.append(local.replace('.', '')+"@"+parts[1])

        return len(set(clean_emails))


