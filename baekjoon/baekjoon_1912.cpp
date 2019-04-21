#include <iostream>

using namespace std;

int MAX(int a, int b) {
	if (a >= b) return a;
	else return b;
}
int main() {

	int n;
	cin >> n;
	int j[100001];
	for (int k = 0; k < n; k++) {
		cin >> j[k];
	}
	int max = j[0];
	
	
	for (int i = 1; i < n; i++) {
		
		j[i] = MAX(j[i], j[i] + j[i - 1]);
		if (j[i] > max) max = j[i];
	}
	cout << max;

}
