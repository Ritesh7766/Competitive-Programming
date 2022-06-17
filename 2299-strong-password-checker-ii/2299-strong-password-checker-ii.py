class Solution:
    def strongPasswordCheckerII(self, password: str) -> bool:
        if len(password) < 8: return False
        
        specials = set([ch for ch in '!@#$%^&*()-+'])
        
        has_upper, has_lower, has_digit, has_special = False, False, False, False
        for i, ch in enumerate(password):
            if ch.isupper(): has_upper = True
            elif ch.islower(): has_lower = True
            elif ch.isdigit(): has_digit = True
            elif ch in specials: has_special = True
            if i > 0 and password[i - 1] == password[i]:
                return False
        
        return has_upper and has_lower and has_digit and has_special