import requests
import random
import time
import argparse

URLS = ["http://192.168.10.21:5000/","http://192.168.10.22:5000/","http://192.168.10.23:5000/"]

def generate_requests(target_urls, total_requests):
	successful_requests = 0
	failed_requests = 0

	for i in range(total_requests):
		target_url = random.choice(target_urls)
		print(f"Sent request {i} to {target_url}: ", end="")
		result = send_request(target_url)
		successful_requests += result
	
	failed_requests = total_requests - successful_requests
	
	print("\nSummary:")
	print(f"Successful: {successful_requests}")
	print(f"Failed: {failed_requests}")
	print(f"Total: {total_requests}")

def send_request(target_url):
	try:
		response = requests.get(target_url)
		if response.status_code == 200:
			print("Success")
			return 1
		else:
			print(f"Failed with status code: {response.status_code}")
			return 0
	
	except requests.exceptions.RequestException as e:
		print(f"Error: {e}")
		return 0

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument(
		"--requests", 
		type=int, 
		default=100, 
		help="Number of requests to send (default: %(default)s)."
	)
	args = parser.parse_args()
	generate_requests(URLS, args.requests)
