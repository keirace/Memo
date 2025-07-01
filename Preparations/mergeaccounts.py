from collections import defaultdict
from typing import List

class Solution:
  # Time complexity: O(n * m * log(m)), where n is the number of accounts and m is the average number of emails per account.
  # Space complexity: O(n + m), where n is the number of accounts and m is the number of unique emails.
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # find parent of an index
        def find(index:int)->int:
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]
        # Union find
        n = len(accounts)
        parent = list(range(n))
        account_id = {}
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in account_id:
                    # Union operation: set the parent of the current account to the account 
                    # already associated with this email.
                    parent[find(i)] = find(account_id[email])
                else:
                    account_id[email] = i
        emails_under_parent_account = defaultdict(set)
        for i, acc in enumerate(accounts):
            for email in acc[1:]:
                emails_under_parent_account[find(i)].add(email)

        merged_accs = []
        for parent_i, emails in emails_under_parent_account.items():
            sorted_emails = sorted(emails)
            account_name = [accounts[parent_i][0]]
            merged_acc = account_name + sorted_emails
            merged_accs.append(merged_acc)
        return merged_accs
    
# Example usage
s = Solution()
accounts = [
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["John", "johnnybravo@mail.com"],
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["Mary", "mary@mail.com"]
]
print(s.accountsMerge(accounts))