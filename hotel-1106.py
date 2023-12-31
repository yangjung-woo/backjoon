import sys


def main():
    c, n = map(int, input().split())
    data = []

    min_cost = [999999999] * (c+100)
    min_cost[0] = 0

    for _ in range(n):
        # cost, cus
        data.append(list(map(int, input().split())))

    # cost 작은 순서로 정리
    data_sort = sorted(data, key = lambda x: x[0])


    for cost, cus in data_sort:
        for i in range(cus, c+100):
            min_cost[i] = min(min_cost[i-cus] + cost, min_cost[i])

    print(min(min_cost[c:]))



if __name__ == '__main__':
    main()