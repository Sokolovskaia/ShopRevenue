from app.shops import the_best_shop_on_total_weekly_revenue, the_best_shop_on_total_weekly_revenue_average, \
    the_best_shop_on_daily_revenue_from_week, the_worst_shop_on_daily_revenue_from_week, top3_sales_of_each_shop


def test_the_best_shop_on_total_weekly_revenue():
    assert [0] == the_best_shop_on_total_weekly_revenue(
        [[2000, 3000, 40000, 50000, 1000, 7000, 100000], [500, 5000, 15000, 20, 7000, 8000, 60000],
         [100, 50000, 1500, 50000, 5000, 10000, 200], [40000, 1000, 500, 300, 15000, 9000, 5000],
         [1500, 300, 15000, 6000, 60000, 15000, 12000]])

    assert [0, 4] == the_best_shop_on_total_weekly_revenue(
        [[2000, 3000, 40000, 50000, 1000, 7000, 100000], [500, 5000, 15000, 20, 7000, 8000, 60000],
         [100, 50000, 1500, 50000, 5000, 10000, 200], [40000, 1000, 500, 300, 15000, 9000, 5000],
         [2000, 3000, 40000, 50000, 1000, 7000, 100000]])


def test_the_best_shop_on_total_weekly_revenue_average():
    assert [0] == the_best_shop_on_total_weekly_revenue_average(
        [[2000, 3000, 40000, 50000, 1000, 7000, 100000], [500, 5000, 15000, 20, 7000, 8000, 60000],
         [100, 50000, 1500, 50000, 5000, 10000, 200], [40000, 1000, 500, 300, 15000, 9000, 5000],
         [1500, 300, 15000, 6000, 60000, 15000, 12000]])

    assert [2, 3] == the_best_shop_on_total_weekly_revenue_average(
        [[40000, 1000, 500, 300, 15000, 9000, 5000], [500, 5000, 15000, 20, 7000, 8000, 60000],
         [100, 50000, 1500, 50000, 5000, 10000, 200], [100, 50000, 1500, 50000, 5000, 10000, 200],
         [1500, 300, 15000, 6000, 60000, 15000, 12000]])





def test_the_best_shop_on_daily_revenue_from_week():
    assert [0] == the_best_shop_on_daily_revenue_from_week(
        [[2000, 3000, 40000, 50000, 1000, 7000, 100000], [500, 5000, 15000, 20, 7000, 8000, 60000],
         [100, 50000, 1500, 50000, 5000, 10000, 200], [40000, 1000, 500, 300, 15000, 9000, 5000],
         [1500, 300, 15000, 6000, 60000, 15000, 12000]])

    assert [0, 3, 4] == the_best_shop_on_daily_revenue_from_week(
        [[2000, 3000, 40000, 50000, 1000, 7000, 100000], [500, 5000, 15000, 20, 7000, 8000, 60000],
         [100, 50000, 1500, 50000, 5000, 10000, 200], [2000, 3000, 40000, 50000, 1000, 7000, 100000],
         [2000, 3000, 40000, 50000, 1000, 7000, 100000]])




def test_the_worst_shop_on_daily_revenue_from_week():
    assert [1] == the_worst_shop_on_daily_revenue_from_week(
        [[2000, 3000, 40000, 50000, 1000, 7000, 100000], [500, 5000, 15000, 20, 7000, 8000, 60000],
         [100, 50000, 1500, 50000, 5000, 10000, 200], [40000, 1000, 500, 300, 15000, 9000, 5000],
         [1500, 300, 15000, 6000, 60000, 15000, 12000]])

    assert [0, 1] == the_worst_shop_on_daily_revenue_from_week(
        [[500, 5000, 15000, 20, 7000, 8000, 60000], [500, 5000, 15000, 20, 7000, 8000, 60000],
         [100, 50000, 1500, 50000, 5000, 10000, 200], [40000, 1000, 500, 300, 15000, 9000, 5000],
         [1500, 300, 15000, 6000, 60000, 15000, 12000]])





def test_top3_sales_of_each_shop():
    assert [[100000, 50000, 40000], [60000, 15000, 8000], [50000, 50000, 10000], [40000, 15000, 9000],
            [60000, 15000, 15000]] == top3_sales_of_each_shop(
        [[2000, 3000, 40000, 50000, 1000, 7000, 100000], [500, 5000, 15000, 20, 7000, 8000, 60000],
         [100, 50000, 1500, 50000, 5000, 10000, 200], [40000, 1000, 500, 300, 15000, 9000, 5000],
         [1500, 300, 15000, 6000, 60000, 15000, 12000]])
