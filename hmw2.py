# # 7.
# filename = input("Fayl nomi: ")
#
# with open(filename) as f:
#     nums = f.read().split()
#
# print(nums[0], nums[1], nums[-2], nums[-1])
#
# # 8.
# f1 = input("Birinchi fayl: ")
# f2 = input("Ikkinchi fayl: ")
#
# if not open(f1).read().strip():
#     print("1-fayl bo‘sh")
# else:
#     with open(f2, "a") as out, open(f1) as inp:
#         lines = inp.read().split()
#         out.write(lines[0] + "\n")
#         out.write(lines[-1] + "\n")
#
# # 9.
# f1 = input("1-fayl: ")
# f2 = input("2-fayl: ")
#
# data = []
#
# if os.path.exists(f1):
#     with open(f1) as a:
#         x = a.read().split()
#         if x:
#             data.append(x[0])
#             data.append(x[-1])
#
# if os.path.exists(f2):
#     with open(f2) as a:
#         x = a.read().split()
#         if x:
#             data.append(x[0])
#             data.append(x[-1])
#
# with open("natija.txt", "w") as out:
#     for d in data:
#         out.write(d + "\n")