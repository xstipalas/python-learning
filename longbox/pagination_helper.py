# TODO: complete this class

class PaginationHelper:
    
    # The constructor takes in an array of items and an integer indicating
    # how many items fit within a single page
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page
    
    # returns the number of items within the entire collection
    def item_count(self):
        return len(self.collection)
    
    # returns the number of pages
    def page_count(self):
        full_pages, last_page = divmod(self.item_count(), self.items_per_page)
        return full_pages + (0, 1)[last_page > 0]
    
    # returns the number of items on the given page. page_index is zero based
    # this method should return -1 for page_index values that are out of range
    def page_item_count(self, page_index):
        page_count = self.page_count()
        
        if page_index > page_count - 1:
            return -1
        elif page_index == page_count - 1:
            return self.item_count() % self.items_per_page
        else:
            return self.items_per_page
    
    # determines what page an item at the given index is on. Zero based indexes.
    # this method should return -1 for item_index values that are out of range
    def page_index(self, item_index):
        if not (0 <= item_index < self.item_count()):
            return -1
        
        prev_pages, cur_page = divmod(item_index + 1, self.items_per_page)
        
        return prev_pages + (0, 1)[cur_page > 0]
