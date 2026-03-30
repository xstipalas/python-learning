def stock_list(stocklist: list[str], categories: list[str]) -> str:
    total = {}
    
    for stock in stocklist:
        code, books = stock.split()
        total[code[0]] = total.get(code[0], 0) + int(books)
    
    if total:
        return ' - '.join(f'({category} : {total.get(category, 0)})' for category in categories)
    else:
        return ''