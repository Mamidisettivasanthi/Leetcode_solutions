class Solution:
    def braceExpansionII(self, expression):
        ans = set()

        def dfs(exp):
            # No braces left
            if '}' not in exp:
                ans.add(exp)
                return

            # Find first closing brace
            j = exp.find('}')

            # Find matching opening brace
            i = exp.rfind('{', 0, j)

            left = exp[:i]
            right = exp[j + 1:]

            # Try every option inside the braces
            for part in exp[i + 1:j].split(','):
                dfs(left + part + right)

        dfs(expression)

        return sorted(ans)