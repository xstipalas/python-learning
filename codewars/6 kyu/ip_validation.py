def is_valid_IP(strng: str) -> bool:
    nums = strng.split('.')
    
    return len(nums) == 4 and all(
        num.isdigit() and
        0 <= int(num) <= 255 and 
        (num == '0' or not num.startswith('0'))
        for num in nums
    )