def make_readable(seconds: int) -> str:
    minutes, res_s = divmod(seconds, 60)
    res_h, res_m = divmod(minutes, 60)
    
    return f"{res_h:02d}:{res_m:02d}:{res_s:02d}"