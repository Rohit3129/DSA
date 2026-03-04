class UF:
    def __init__(self, N):
        self.parents = [i for i in range(N)]

    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))

        # STEP 1) Create unions between indexes----------------------------------------
        # map from every email -> its corresponding owner index
        ownership = {}

        # '_' is the name (ignored here). iterate thru all accounts and their emails
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:

                # if one of the emails from the account was already seen in a diff account
                if email in ownership:
                    # set union between the owner index and the existing owner index (may be redundant)
                    uf.union(i, ownership[email])

                # populate the map of every email to its owner index
                ownership[email] = i

        # STEP 2) Append emails to correct index----------------------------------------
        # map from owner index -> all emails by that owner 
        ans = collections.defaultdict(list)
        # iterate thru every email seen
        for email, owner in ownership.items():
            # use union find to merge owners, while appending email to the owner's list of emails
            ans[uf.find(owner)].append(email)

        # for every merged owner and email list in ans, 
        # fetch the string name of the owner index using input param 'accounts', and sort the emails
        return [[accounts[i][0]] + sorted(emails) for i, emails in ans.items()]