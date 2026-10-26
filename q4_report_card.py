scores = {
    "Ali": 18, 
    "Sara": 20, 
    "Reza": 9, 
    "Mina": 14, 
    "Omid": 11.5
}

print("--- کارنامه دانش‌آموزان ---")
passed_count = 0
total_score = 0

for name, score in scores.items():
    total_score += score
    if score >= 10:
        status = "قبولی"
        passed_count += 1
    else:
        status = "مردودی"
    
    print(f"{name}: {score} -> {status}")

average_score = total_score / len(scores)
top_student = max(scores, key=scores.get)

print("-" * 30)
print(f"میانگین نمرات کلاس: {average_score:.2f}")
print(f"دانش‌آموز برتر: {top_student} با نمره {scores[top_student]}")
print(f"تعداد قبول‌شدگان: {passed_count} از {len(scores)}")