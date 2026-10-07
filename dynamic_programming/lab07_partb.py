# Part B (Packing Supplies):
# * recursively, I might say the maximum value for the next rocket is
#   the maximum of (include item i (v_i) + optimal(exclude item i, W - w_i),
#                   optimal(exclude item i, W))

# **you do not need to do this for Lab 07**
class SpaceCargo():
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight

def max_rocket_value(items, max_weight):
    if len(items) == 0:
        return 0

    include_item_value = 0
    if items[0].weight <= max_weight:
        include_item_value = items[0].value + \
                        max_rocket_value(items[1:], max_weight - items[0].weight)
        
    exclude_item_value = max_rocket_value(items[1:], max_weight)

    return max(include_item_value, exclude_item_value)

if __name__=='__main__':
    item1 = SpaceCargo(10, 5)
    item2 = SpaceCargo(5, 1)

    print(max_rocket_value([item1, item2], 5))