
#
# def test(differences, lower, upper):
#
#     res = 0
#     memo = {}
#     for num in range(lower, upper+1):
#         res += dfs(0, num, differences, lower, upper, memo)
#     return res
#
# def dfs(i, num, differences, lower, upper, memo):
#
#     if (i, num) in memo:
#         return memo[(i, num)]
#     n = len(differences)
#     if i >= n:
#         return 1
#
#     new_num = num + differences[i]
#     if new_num < lower:
#         return 0
#     if new_num > upper:
#         return 0
#
#     count = 0
#     count += dfs(i+1, new_num, differences, lower, upper, memo)
#     memo[(i, num)] = count
#     return count
#
#
#
# differences = [3,-4,5,1,-2]
# lower = -4
# upper = 5
#
#
# # differences = [1, -3, 4]
# # lower = 1
# # upper = 6
# print(test(differences, lower, upper))


from datetime import datetime
time = datetime.now()

print(time.minute + time.hour * 60 + time.day * 60 * 24 )

#
# def connectTwoGroups(send_orders,pickup_orders):
#     # connect all left nodes to the right
#     # connect remaining right nodes to the left (preprocessing min cost of connecting right node to left node)
#     m, n = len(send_orders), len(pickup_orders)
#     weight = [[0]* n for _ in range(m)]
#     for i, s_order in enumerate(send_orders):
#         s_order_id, s_car_type, s_book_time, s_airport_name = s_order.split(",")
#         datetime_object = datetime.strptime(s_book_time, '%y/%m/%d %H:%M:%S')
#         # print(datetime_object.minute)
#         for j, p_order in enumerate(pickup_orders):
#             p_order_id, p_car_type, p_book_time, p_airport_name = p_order.split(",")
#             # idle = p_book_time - s_book_time
#             # weight[i, j] = idle
#     print(weight)
#     return
#
# send_orders=[
# "_order1,1,2022-02-11 12:00:00, airporti",
# "S_order2,1,2022-02-11 12:30:00, airporti",
# "_order3,1,2022-02-11 12:10:00,airport1",
# "_order4,2,2022-02-12 12:30:00,airport2",
# "S_order5,2,2022-02-12 18:27:00,airport2",
# "_order6,1,2022-02-12 19:30:00, airport2",
# "_order7,2,2022-02-12 20:15:00, airport2",
# ]
# pickup_orders =[
# "p_order1,1,2022-02-11 12:20:00, airport1",
# "p_order2,2,2022-02-11 14:30:00,airporti",
# "p_order3,2,2022-02-12 12:45:00, airport2",
# "p_order4,2,2022-02-12 12:15:00, airport2",
# "p_order5,2,2022-02-12 19:20:00,airport2",
# "p_order6,2,2022-02-12 20:30:00,airport2",
# "p_order7,2,2022-02-12 20:00:00, airport2"
# ]
# print(connectTwoGroups(send_orders, pickup_orders))
#
#


