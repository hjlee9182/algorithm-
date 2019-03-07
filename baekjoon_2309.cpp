#include <iostream>
#include <algorithm>
#include <vector>
#include <stdio.h>



using namespace std;

int main() {
	
	int a,sum=0;
	vector<int> arr(9);
	for (int i = 0; i < 9; i++) {

		scanf("%d", &a);
		arr[i] = a;
		sum += a;
	}
	
	for (int j = 0; j < 9; j++) {
		for (int k = j+1; k < 9; k++) {
			if ((sum - arr[j] - arr[k]) == 100) {
				arr.erase(arr.begin() + j);
				arr.erase(arr.begin() + k-1);
				sort(arr.begin(), arr.end());
				for (int q = 0; q < 7; q++) {
					cout << arr[q]<<endl;
					
				}
				system("pause");
				return 0;
			}
		}
	}

	system("pause");
	return 0;
}
