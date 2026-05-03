def analyze_reviews():
	reviews_file = "reviews.txt"
	if not os.path.exists(reviews_file):
		print(f"Error: {reviews_file} not found.")
		return
	with open(reviews_file, 'r') as f:
		content = f.read()
	total_characters = len(content)
	reviews = content.splitlines()
	total_reviews = len(reviews)
	good_count = 0
	bad_count = 0
	for review in reviews:
		review_lower = review.lower()
		if "good" in review_lower:
			good_count += 1
		if "bad" in review_lower:
			bad_count += 1
	if total_reviews > 0:
		percentage = round((good_count / total_reviews) * 100, 2)
	else:
		percentage = 0.0
	if percentage >= 70:
		rating = "Positive"
	elif 40 <= percentage < 70:
		rating = "Mixed"
	else:
		rating = "Negative"
	result = f"""Review Text Analysis
Total Characters: {total_characters}
Good Reviews: {good_count}
Bad Reviews: {bad_count}
Percentage of Good Reviews: {percentage}%
Overall Rating: {rating}
	print(result)
	with open("review_results.txt", 'w') as f:
		f.write(result)

if __name__ == "__main__":
	analyze_reviews()