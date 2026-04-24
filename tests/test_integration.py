from main import calculate_total, apply_tax

def test_total_with_tax():
    items = [100, 200, 300]
    total = calculate_total(items)
    final_total = apply_tax(total, 0.1)

    assert final_total == 660