
class Solution:
    def filterRestaurants(self, restaurants, veganFriendly, maxPrice, maxDistance):
        restaurants.sort(key=lambda x: (-x[1], -x[0]))
        return [i for i, r, v, p, d in restaurants if v >= veganFriendly and p <= maxPrice and d <= maxDistance]

