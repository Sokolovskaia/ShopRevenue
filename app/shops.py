def the_best_shop_on_total_weekly_revenue(weekly_revenue):  # 1
    amount_for_week = []
    for shop_revenue in weekly_revenue:
        amount_for_week.append(sum(shop_revenue))
    best_shops = []
    for shop_index, amount in enumerate(amount_for_week):
        if amount == max(amount_for_week):
            best_shops.append(shop_index)
    return best_shops


def the_best_shop_on_total_weekly_revenue_average(weekly_revenue):  # 2
    amount_for_week = []
    for shop_revenue in weekly_revenue:
        amount_for_week.append(sum(shop_revenue) / len(shop_revenue))
    best_shops = []
    for shop_index, amount in enumerate(amount_for_week):
        if amount == max(amount_for_week):
            best_shops.append(shop_index)
    return best_shops


def the_best_shop_on_daily_revenue_from_week(weekly_revenue):  # 3
    max_revenue_all = []
    for shop_revenue in weekly_revenue:
        max_revenue_all.append(max(shop_revenue))
    best_shops = []
    for shop_index, max_revenue in enumerate(max_revenue_all):
        if max_revenue == max(max_revenue_all):
            best_shops.append(shop_index)
    return best_shops


def the_worst_shop_on_daily_revenue_from_week(weekly_revenue):  # 4
    min_revenue_all = []
    for shop_revenue in weekly_revenue:
        min_revenue_all.append(min(shop_revenue))
    worst_shops = []
    for shop_index, min_revenue in enumerate(min_revenue_all):
        if min_revenue == min(min_revenue_all):
            worst_shops.append(shop_index)
    return worst_shops


def top3_sales_of_each_shop(weekly_revenue):  # 5
    for shop_revenue in weekly_revenue:
        shop_revenue.sort(reverse=True)
    top3_shop = []
    for shop_revenue in weekly_revenue:
        top3_shop.append(shop_revenue[:3])

    return top3_shop

